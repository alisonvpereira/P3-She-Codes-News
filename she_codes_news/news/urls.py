from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    # path('mystories/', views.StoryListView.as_view(), name='myStories'),
    path('storylist/', views.StoryListView.as_view(), name='storyList'),
]