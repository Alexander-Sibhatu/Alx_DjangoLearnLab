from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:   
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None
    
def get_books_in_Library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)

        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        None