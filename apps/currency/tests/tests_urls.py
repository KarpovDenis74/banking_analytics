from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class CurrencyURLTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='NameUser1')
        cls.authorized_client = Client()
        # Авторизуем пользователя
        cls.authorized_client.force_login(cls.user)

    def tests_url_currency_guest_client(self):
        """Страница /currency/ доступна любому пользователю."""
        response = CurrencyURLTest.guest_client.get(reverse('currency:index'))
        self.assertEqual(response.status_code, 200)

    def tests_url_currency_authorized_client(self):
        """Страница /currency/ доступна любому пользователю."""
        response = CurrencyURLTest.authorized_client.get(
            reverse('currency:index'))
        self.assertEqual(response.status_code, 200)
