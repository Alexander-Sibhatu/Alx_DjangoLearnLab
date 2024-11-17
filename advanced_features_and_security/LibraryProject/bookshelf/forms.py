from django import forms
from .models import Book


class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter title',
            'class': 'form-control',
        }),
        label="Title"
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter description',
            'class': 'form-control',
            'rows': 3,
        }),
        label="Description",
        required=False
    )
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        }),
        label="Publication Date",
        required=True
    )
