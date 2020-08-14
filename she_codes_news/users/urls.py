from django.urls import path
# from .views import CreateAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='create-account'),
    path('<int:pk>/', views.UserProfileView.as_view(), name='user-detail'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
 
    
]