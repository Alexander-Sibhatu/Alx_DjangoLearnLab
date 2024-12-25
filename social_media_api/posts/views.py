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
    permission_classes = [permissions.IsAuthenticated]
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
    
# Like Functionality
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Like
from notifications.models import Notification
from rest_framework import generics

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Safely fetch the post or return a 404 error
        post = generics.get_object_or_404(Post, pk=pk)

        # Attempt to create a like, ensuring no duplicates
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        if request.user != post.author:  # Avoid notifying the author if they like their own post
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )

        return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        # Safely fetch the post or return a 404 error
        post = generics.get_object_or_404(Post, pk=pk)

        # Find the like instance
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({'error': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()
        return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)