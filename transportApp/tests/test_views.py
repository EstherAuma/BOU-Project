from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail

class TestChangePasswordView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_change_password_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Get the change password URL
        url = reverse('change_password')  # Replace 'change_password' with the actual URL name

        # Make a POST request to change the password
        response = self.client.post(url, {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
            'username': 'testuser',
            'email': 'testuser@example.com',
        })

        # Check if the response is a redirect to the login page
        self.assertRedirects(response, reverse('login'))  # Replace 'login' with the actual URL name

        # Check if the user's password has been changed
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newtestpassword'))

        # Check if an email has been sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Change password')

    def tearDown(self):
        self.client.logout()
