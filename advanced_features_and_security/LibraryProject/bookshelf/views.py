from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render, redirect
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

# def example_view(request):
#     if request.method == 'POST':
#         form = ExampleForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             publication_date = form.cleaned_data['publication_date']
#             # You can now save data or process it as needed
#             return render(request, 'bookshelf/success.html', {'form': form})
#     else:
#         form = ExampleForm()
#     return render(request, 'bookshelf/example_form.html', {'form': form})

def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here
            print("Form submitted successfully!")
            return render(request, 'bookshelf/success.html', {'form': form})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def book_list_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})