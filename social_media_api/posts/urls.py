from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, PostViewSet, FollowingPostsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('posts/', PostViewSet.as_view(), name='posts'),
    path('feed/', FollowingPostsView.as_view(), name='feed')
]

