from django.views import generic
from .models import NewsStory, PUBLISH
from django.urls import reverse_lazy
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

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
        context['latest_stories'] = NewsStory.objects.filter(status=PUBLISH).order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.filter(status=PUBLISH).order_by('-pub_date')
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

class StoryUpdateView(generic.UpdateView):
    model = NewsStory
    # form_class = CustomUserChangeForm
    fields = '__all__'
    template_name = 'news/story_update.html'

class AuthorListView(generic.ListView):
    model = User
    template_name = 'news/author_list.html'
    context_object_name = 'author_list'

class AuthorDetailView(generic.DetailView):
    model = User
    template_name = 'users/userprofile.html'
    context_object_name = 'user-detail'
