from .views import BookList
from django.urls import path

urlpatters = [
    path('book/', BookList.as_view(), name='book-list')
]