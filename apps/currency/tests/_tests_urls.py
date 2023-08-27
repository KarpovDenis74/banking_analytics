from http import HTTPStatus

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
        cls.admin = User.objects.create_user(username='Admin1', is_staff=True)
        cls.admin_client = Client()
        # Авторизуем пользователя
        cls.admin_client.force_login(cls.admin)

    def test_index_guest_client(self):
        """Страница /currency/ доступна любому пользователю."""
        response = CurrencyURLTest.guest_client.get(reverse('currency:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK.value)

    def test_index_authorized_client(self):
        """Страница /currency/ доступна авторизованному пользователю."""
        response = CurrencyURLTest.authorized_client.get(
            reverse('currency:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK.value)

    def test_get_currency_for_day(self):
        """
            Страница /currency/get_currency_for_day/
            доступна только администратору:
                - авторизованный пользователь (не админ) перенаправляется
                  на главную страницу
                - не авторизованный перенаправляется на страницу
                  авторизации
        """
        response = CurrencyURLTest.admin_client.get(
            reverse('currency:get_currency_for_day'))
        self.assertEqual(response.status_code, HTTPStatus.OK.value)
        response = CurrencyURLTest.guest_client.get(
            reverse('currency:get_currency_for_day'))
        reverse1 = reverse('login')
        reverse2 = reverse('currency:get_currency_for_day')
        self.assertRedirects(response,
                             expected_url=f'{reverse1}?next={reverse2}',
                             status_code=HTTPStatus.FOUND.value,
                             target_status_code=HTTPStatus.OK.value,
                             msg_prefix='',
                             fetch_redirect_response=False
                             )
        response = CurrencyURLTest.authorized_client.get(
            reverse('currency:get_currency_for_day'))
        self.assertRedirects(response,
                             reverse('core:index'))

    # def test_urls_uses_correct_template(self):
    #     """URL-адрес использует соответствующий шаблон."""
    #     templates_url_names = {
    #         reverse('currency:index'): 'currency/currency.html',
    #         reverse('currency:get_currency_for_day'): (
    #             'currency/get_currency_for_day.html'
    #         )
    #     }
    #     for address, template in templates_url_names.items():
    #         with self.subTest(address=address):
    #             response = self.admin_client.get(address)
    #             self.assertTemplateUsed(response, template)
