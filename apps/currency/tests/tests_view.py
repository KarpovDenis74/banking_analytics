import datetime

from apps.currency.models import Currency, CurrencyRate
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class CurrencyViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='NameUser1')
        cls.authorized_client = Client()
        # Авторизуем пользователя
        cls.authorized_client.force_login(cls.user)
        cls.currency = Currency.objects.create(num_code=840,
                                               char_code='USD',
                                               name='Доллар США')
        rate_date = datetime.date.today()
        cls.cur_rate = CurrencyRate.objects.create(date=rate_date,
                                                   currency=cls.currency,
                                                   value=1.2, nominal=100)

    def test_currency_page_show_correct_context(self):
        """Шаблон currency сформирован с правильным контекстом."""
        rate_date = datetime.date.today().strftime("%Y-%m-%d")
        response = CurrencyViewsTest.guest_client.get(
            reverse('currency:index'))
        self.assertEqual(response.context.get('title'), 'Курсы валют')
        self.assertEqual(response.context.get('header'), 'Курсы валют')
        self.assertEqual(response.context.get('rate_date'), rate_date)
        self.assertEqual(response.context.get('currency')[0].num_code, 840)
        self.assertEqual(response.context.get(
            'currency_rate')[0].value, 1.2)
