from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FollowingPostsView(generics.ListAPIView):
    permissions_class = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
         # Get the list of users the current user is following
        following_users = self.request.user.following.all()
        # Filter posts authored by those users and order them by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)