from django.urls import path
from .views import example_view
from .views import form_example_view
from .views import book_list_view

urlpatterns = [
    path('example-form/', example_view, name='example_form'),
    path('form-example/', form_example_view, name='form_example'),
    path('book-list/', book_list_view, name='book_list'),
]
