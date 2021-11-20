

from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='dunitt', 
            email='dunitt@example.com', 
            password='testpass123', 
        )
        self.assertEqual(user.username, 'dunitt')
        self.assertEqual(user.email, 'dunitt@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='super_dunitt', 
            email='super_dunitt@example.com', 
            password='testpass123', 
        )
        self.assertEqual(user.username, 'super_dunitt')
        self.assertEqual(user.email, 'super_dunitt@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

