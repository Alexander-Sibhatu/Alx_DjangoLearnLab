# CRUD Operations on Book Model

## Create Operation

**Command:**

```python
from bookshelf.models import Book
new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
) 
new_book
```


### Expected Output: 1984 by George Orwell


## Retrieve Operation

**command**

```book = Book.objects.get(id=new_book.id)
book
```

### Expected Output: 1984 by George Orwell


## Update Operation

```book.title = "Nineteen Eighty-Four"
book.save()
book
```

### Expected Output: Nineteen Eighty-Four by George Orwell

## Delete Operation

**Command**

```book.delete()
Book.objects.all() 
```

### Expected Output: (1, {'bookshelf.Book': 1})
<QuerySet []>
