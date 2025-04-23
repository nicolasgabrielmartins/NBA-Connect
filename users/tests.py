# PARA RODAR --> python manage.py test users

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile

class UserRegistrationTest(TestCase):
    def test_register_user_with_avatar(self):
        avatar = SimpleUploadedFile("avatar.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'bio': 'Bio de teste',
            'favorite_team': 'Lakers',
            'avatar': avatar
        })

        self.assertEqual(response.status_code, 302)  # redirecionamento
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.bio, 'Bio de teste')
        self.assertEqual(profile.favorite_team, 'Lakers')
        self.assertTrue(profile.avatar.name.startswith('avatar/'))

