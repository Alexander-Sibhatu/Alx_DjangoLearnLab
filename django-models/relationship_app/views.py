# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app.models import Book
from django.views.generic.detail import DetailView
from .models import Library, UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after successful registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View (Using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View (Using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'member_view.html')
