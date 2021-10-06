from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.deletion import CASCADE

User = get_user_model()


class Currency(models.Model):
    num_code = models.PositiveSmallIntegerField(
        verbose_name='Цировой код валюты',
        unique=True,
        blank=False,
        help_text='Дайте валюте цировой код'
    )
    char_code = models.CharField(
        verbose_name='Символьный код валюты',
        max_length=10,
        unique=True,
        blank=False,
    )
    name = models.CharField(
        verbose_name='Наименование валюты',
        max_length=256,
        blank=False,
    )

    class Meta:
        verbose_name = 'Иностранная валюта'
        verbose_name_plural = 'Иностранные валюты'
        ordering = ['num_code']

    def __str__(self):
        return f'{self.num_code}: {self.name}'


class CurrencyRate(models.Model):
    date = models.DateField(
        verbose_name='Курс валюты на дату',
        blank=False,
        help_text='Дата установки курса',
    )
    currency = models.ForeignKey(
        Currency,
        verbose_name='валюта',
        on_delete=CASCADE,
        blank=False,
    )
    value = models.FloatField(
        verbose_name='Значение курса валюты',
        blank=False,
    )
    nominal = models.PositiveSmallIntegerField(
        verbose_name='Номинал валюты',
        blank=False,
    )

    class Meta:
        UniqueConstraint(fields=['date', 'currency'],
                         name='unique_date_currency')
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        ordering = ['-date']

    def __str__(self):
        return f'{self.value}'
