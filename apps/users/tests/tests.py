from django.test import Client, TestCase
from apps.users.models import User


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
