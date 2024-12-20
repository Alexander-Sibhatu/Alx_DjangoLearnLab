from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

# forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = TagWidget(
                attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas'}
                )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
        if 'tags' in self.cleaned_data:
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
            instance.tags.set(*tag_names) # Uses TaggableManager's set method to assign tags
        return instance

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

