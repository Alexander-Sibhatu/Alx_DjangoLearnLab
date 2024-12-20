from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CommentForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from .models import Post, Comment
from django.views.generic import View

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reistration successful! You can now log in.')
            return redirect('login')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'registration/profile.html')

# Create your views here.

# views.py
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to home after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Implement Comment views
class CommentCreateView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
        return render(request, 'blog/post_detail.html', {'form': form, 'post': post})
    

class CommentUpdateView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
        return render(request, 'blog/edit_comment.html', {'form': form})
    
class CommentDeleteView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', post_id=post_id)