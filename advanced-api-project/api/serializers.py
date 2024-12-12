from rest_framework import serializers
from .models import Author, Book

class BookSerlializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerlializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]