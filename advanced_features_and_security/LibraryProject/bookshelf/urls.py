from django.urls import path
from .views import example_view
from .views import form_example_view

urlpatterns = [
    path('example-form/', example_view, name='example_form'),
    path('form-example/', form_example_view, name='form_example'),
]
