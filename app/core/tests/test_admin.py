"""
Test for the Django Admin modifications
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Test for Django Admin"""

    def setUp(self):
        """Create user and client"""

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser (
            email='admin@example.com',
            password='pasword123',
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user (
            email='testuser@example.com',
            password='password123',
            name='Test User',
        )

    def test_users_list(self):
        """Test if the user list is being returned"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)