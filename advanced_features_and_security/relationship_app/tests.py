# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from django.db.models.signals import post_save
from .signals import create_user_profile, save_user_profile

class RoleBasedAccessTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Disconnect signals to avoid auto-creation of UserProfile
        post_save.disconnect(create_user_profile, sender=User)
        post_save.disconnect(save_user_profile, sender=User)

    def setUp(self):
        # Manually create users and assign roles
        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        UserProfile.objects.create(user=self.admin_user, role='Admin')
        
        self.librarian_user = User.objects.create_user(username='librarian', password='librarian123')
        UserProfile.objects.create(user=self.librarian_user, role='Librarian')
        
        self.member_user = User.objects.create_user(username='member', password='member123')
        UserProfile.objects.create(user=self.member_user, role='Member')

    @classmethod
    def tearDownClass(cls):
        # Reconnect the signals after tests
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_user_profile, sender=User)
        super().tearDownClass()

    def test_admin_view_access(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='librarian', password='librarian123')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)

        self.client.login(username='member', password='member123')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)

    def test_librarian_view_access(self):
        self.client.login(username='librarian', password='librarian123')
        response = self.client.get(reverse('librarian_view'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('librarian_view'))
        self.assertEqual(response.status_code, 403)

        self.client.login(username='member', password='member123')
        response = self.client.get(reverse('librarian_view'))
        self.assertEqual(response.status_code, 403)

    def test_member_view_access(self):
        self.client.login(username='member', password='member123')
        response = self.client.get(reverse('member_view'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('member_view'))
        self.assertEqual(response.status_code, 403)

        self.client.login(username='librarian', password='librarian123')
        response = self.client.get(reverse('member_view'))
        self.assertEqual(response.status_code, 403)
