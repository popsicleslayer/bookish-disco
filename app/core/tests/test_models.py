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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'password123')
            self.assertEqual(user.email, expected)