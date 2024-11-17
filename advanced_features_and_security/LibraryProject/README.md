# Django Development Environment Setup

## Permissions and Groups in Django

### Groups
- **Editors:** Can edit and create books.
- **Viewers:** Can view books only.
- **Admins:** Can view, create, edit, and delete books.

### Permissions
Permissions added to the `Book` model:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

### Views
- `book_list`: Requires `can_view`.
- `create_book`: Requires `can_create`.
- `edit_book`: Requires `can_edit`.
- `delete_book`: Requires `can_delete`.

### Setup
Run the following command to set up groups and permissions:
```bash
python manage.py setup_groups
