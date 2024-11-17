from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'required': True, 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'required': True, 'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'required': True}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("The title must be at least 3 characters long.")
        return title
