# Retrieve Operation

**Command:**

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book

Expected Output:
<Book: 1984 by George Orwell>
