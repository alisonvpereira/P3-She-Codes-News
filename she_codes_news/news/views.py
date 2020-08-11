from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # return render(request, 'users/createAccount.html', {'form': form})
    

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.filter(status__exact=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class StoryListView(LoginRequiredMixin, generic.ListView):
    model = NewsStory
    template_name ='news/storylist.html'
    context_object_name = 'story_list'
    paginate_by = 10
    
    def get_queryset(self):
        return NewsStory.objects.filter(author=self.request.user).order_by('pub_date')


