from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, PostViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('posts/', PostViewSet.as_view(), name='posts'),
]

# from rest_framework.routers import DefaultRouter
# from .views import PostViewSet, CommentViewSet

# router = DefaultRouter()
# router.register('posts', PostViewSet, basename='post')
# router.register('comments', CommentViewSet, basename='comment')

# urlpatterns = router.urls