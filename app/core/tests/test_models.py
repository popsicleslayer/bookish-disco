"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import  get_user_model


class ModelTests(TestCase):
    """Tests models"""

    def tests_create_user_with_email_successful(self):
        """Tests successfully creating a suer with an email address"""
        email = "test@example.com"
        password = "123password"
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))