from django.urls import path
from .views import BookListView, BookDetailView, CreateView, UpdateView, DeleteView

urlpatters = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail')
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/update', UpdateView.as_view(), name='update-book'),
    path('books/delete', DeleteView.as_view(), name='delete-book'),
]

