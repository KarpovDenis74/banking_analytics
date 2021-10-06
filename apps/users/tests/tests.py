from django.conf import settings
from django.test import Client, TestCase
from users.models import User


class TestPosts(TestCase):
    def setUp(self):
        self.client_on = Client()
        self.client_off = Client()
        self.user = User.objects.create(
            username='test_user', email='q@q.com')
        self.user.set_password('123')
        self.user.save()
        self.client_on.force_login(self.user)
        self.clients = (self.client_on, self.client_off,)

    def test_check_debug(self):
        self.assertEqual(settings.DEBUG, False)
