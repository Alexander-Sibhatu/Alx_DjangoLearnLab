from django.shortcuts import render
from relationship_app.models import Book

# Create your views here.
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
