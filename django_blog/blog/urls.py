from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlspatters = [
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='templates/logout.html'),
          name='logout'),
    path('register/', auth_views.LogoutView.as_view(template_name='templates/register.html'),
          name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('', auth_views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', auth_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', auth_views.PostCreateView.as_view(), name='post-edit'),
    path('post/<int:pk>/update/', auth_views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', auth_views.PostDeleteView.as_view(), name='post-delete'),
     path('posts/<int:post_id>/comments/new/', auth_views.CommentCreateView.as_view(), name='create_comment'),
    path('comments/<int:comment_id>/edit/', auth_views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:comment_id>/delete/', auth_views.CommentDeleteView.as_view(), name='delete_comment'),
]