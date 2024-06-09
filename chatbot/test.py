from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpTests(TestCase):
    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_process(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())
