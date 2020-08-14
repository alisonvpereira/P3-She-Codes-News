from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('storylist/<slug:slug>/', views.StoryListView.as_view(), name='storyList'),
    path('<int:pk>/update/', views.StoryUpdateView.as_view(), name='story_update'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    
]
