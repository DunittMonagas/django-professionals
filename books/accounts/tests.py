

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='admin', 
            email='admin@example.com', 
            password='testpass123', 
        )
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='super_admin', 
            email='super_admin@example.com', 
            password='testpass123', 
        )
        self.assertEqual(user.username, 'super_admin')
        self.assertEqual(user.email, 'super_admin@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 
            'Hi there! I should not be on the page.'
        )

    def test_signup_form(self):

        User = get_user_model()
        User.objects.create_user(
            self.username, 
            self.email
        )

        new_user = User.objects.first()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(new_user.username, self.username)
        self.assertEqual(new_user.email, self.email)
        
