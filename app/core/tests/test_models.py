from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@kondosoft.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        """TEST CREATING WITH AN EMAIL SUCCESS"""
        email = 'luismanueljf@gmail.com'
        password = 'rt459pk1'
        user = get_user_model().objects.create_user(
          email=email,
          password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'luismanuel@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'password123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """TEST CREATING USER WITH NO EMAIL RAISES ERROR"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
          'test@gmail.com',
          'password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
