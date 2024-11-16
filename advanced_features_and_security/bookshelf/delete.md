# Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book instance first to delete it
book = Book.objects.get(title="1984")
book.delete()

# Confirm deletion by checking all books
Book.objects.all()


