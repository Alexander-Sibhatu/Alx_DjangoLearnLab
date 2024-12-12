from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return f"{self.title} {self.publication_year}"

from rest_framework import serializers

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