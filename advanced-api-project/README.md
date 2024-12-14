### Book API Endpoints

- **GET /api/books/**: List all books with optional filtering, searching, and ordering.
  - **Filtering**: Filter by `title`, `author`, or `publication_year`.
    - Example: `/api/books/?title=Python`
    - Example: `/api/books/?author=John Doe`
  - **Searching**: Search `title` and `author`.
    - Example: `/api/books/?search=python`
  - **Ordering**: Order results by `title` or `publication_year`.
    - Example: `/api/books/?ordering=title`
    - Example: `/api/books/?ordering=-publication_year`
  - **Combining filters, search, and ordering**:
    - Example: `/api/books/?author=John Doe&ordering=publication_year`


### Unit Testing for Book API

- **Test CRUD Operations**: Verifies that authenticated users can create, update, and delete books while unauthenticated users are restricted.
- **Test Filtering**: Validates filtering functionality based on the `title` field.
- **Test Searching**: Ensures that the search functionality works as expected for `title` and `author`.
- **Test Ordering**: Confirms that books can be ordered by `publication_year`.
- **Test Authentication**: Checks that permissions are properly enforced on all CRUD operations.

To run the tests, use the command: `python manage.py test api`.
