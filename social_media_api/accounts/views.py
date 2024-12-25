from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _= Token.objects.get_or_create(user=user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        user_to_follow_id = kwargs.get('user_id')
        user_to_foolow = CustomUser.objects.filter(id=user_to_follow_id)
        if not user_to_foolow:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        request.user.following.add(user_to_foolow)
        return Response({'message': f'You are now following {user_to_foolow.username}.'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        user_to_unfollow_id = kwargs.get('user_id')
        user_to_unfollow = CustomUser.objects.filter(id=user_to_unfollow_id).first()
        if not user_to_unfollow:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)