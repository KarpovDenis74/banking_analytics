from datetime import datetime as dt

from apps.currency.models import Currency, CurrencyRate
from django.test import TestCase


class CurrencyModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_verboses = {
            'num_code': 'Цировой код валюты',
            'char_code': 'Символьный код валюты',
            'name': 'Наименование валюты',
        }
        cls.field_help = {
            'num_code': 'Дайте валюте цировой код'
        }
        cls.num_code = 1
        cls.char_code = 'USD',
        cls.name = 'Доллар США'
        # Создаём тестовую запись в БД
        # и сохраняем созданную запись в качестве переменной класса
        cls.currency = Currency.objects.create(
            num_code=cls.num_code,
            char_code=cls.char_code,
            name=cls.name
        )

    def test_fields_label(self):
        """___ verbose_name полей модели  Currency совпадает с ожидаемым."""
        currency = CurrencyModelTest.currency
        for field, value in CurrencyModelTest.field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    currency._meta.get_field(field).verbose_name, value)

    def test_help_text_fields(self):
        """___ help_text полeй модели Currency совпадает с ожидаемым."""
        currency = CurrencyModelTest.currency
        for field, value in CurrencyModelTest.field_help.items():
            with self.subTest(field=field):
                self.assertEqual(
                    currency._meta.get_field(field).help_text, value)

    def test_str_method(self):
        """__str__  =>  f'{self.num_code}: {self.name}'"""
        currency = CurrencyModelTest.currency  # Обратите внимание на синтаксис
        self.assertEqual(
            str(currency),
            f'{CurrencyModelTest.num_code}: {CurrencyModelTest.name}'
        )


class CurrencyRateModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_verboses = {
            'date': 'Курс валюты на дату',
            'value': 'Значение курса валюты',
            'nominal': 'Номинал валюты',
        }
        cls.field_help = {
            'date': 'Дата установки курса',
        }
        cls.num_code = 2
        cls.char_code = 'EURO',
        cls.name = 'Евро'
        # Создаём тестовую запись в БД
        # и сохраняем созданную запись в качестве переменной класса
        cls.currency = Currency.objects.create(
            num_code=cls.num_code,
            char_code=cls.char_code,
            name=cls.name
        )
        cls.date = dt.today()
        cls.value = 12.3
        cls.nominal = 100
        cls.currency_rate = CurrencyRate.objects.create(
            date=cls.date,
            value=cls.value,
            nominal=cls.nominal,
            currency=cls.currency
        )

    def test_fields_label(self):
        """
            ___ verbose_name полей модели  CurrencyRate совпадает с ожидаемым.
        """
        currency_rate = CurrencyRateModelTest.currency_rate
        for field, value in CurrencyRateModelTest.field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    currency_rate._meta.get_field(field).verbose_name, value)

    def test_help_text_fields(self):
        """___ help_text полeй модели Currency совпадает с ожидаемым."""
        currency_rate = CurrencyRateModelTest.currency_rate
        for field, value in CurrencyRateModelTest.field_help.items():
            with self.subTest(field=field):
                self.assertEqual(
                    currency_rate._meta.get_field(field).help_text, value)

    def test_str_method(self):
        """__str__  =>  f'{self.num_code}: {self.name}'"""
        currency_rate = CurrencyRateModelTest.currency_rate
        self.assertEqual(
            str(currency_rate),
            f'{CurrencyRateModelTest.value}'
        )
