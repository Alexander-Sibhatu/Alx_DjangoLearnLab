from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2021
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book_authenticated(self):
        # Test creating a book with authentication
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
    
    def test_create_book_unauthenticated(self):
        # Test creating a book without authentication
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_book_authenticated(self):
        # Test updating a book with authentication
        self.client.login(username='testuser', password='password123')
        updated_data = {'title': 'Updated Book Title'}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
    
    def test_update_book_unauthenticated(self):
        # Test updating a book without authentication
        updated_data = {'title': 'Updated Book Title'}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete_book_authenticated(self):
        # Test deleting a book with authentication
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_book_unauthenticated(self):
        # Test deleting a book without authentication
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_book_filtering(self):
        # Test filtering books by title
        response = self.client.get(reverse('book-list') + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_book_search(self):
        # Test searching books by title
        response = self.client.get(reverse('book-list') + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_book_ordering(self):
        # Test ordering books by publication_year
        response = self.client.get(reverse('book-list') + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)

