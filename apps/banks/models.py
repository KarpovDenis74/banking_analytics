from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bank(models.Model):
    long_name = models.CharField(
        verbose_name="Официальное польное наименование",
        max_length=1000,
    )
    short_name = models.CharField(
        verbose_name="Официальное сокращенное наименование",
        max_length=500,
    )
    bic = models.CharField(
        max_length=9,
        verbose_name="Код BIC кредитной организации",
    )
    reg_date = models.DateField(
        verbose_name="Дата регистрации кредитной организации в ЦБ",
    )
    name = models.CharField(
        verbose_name="Наименование кредитной организации",
        max_length=256,
    )
    ogrn = models.CharField(
        verbose_name="Основной государственный регистрационный номер",
        max_length=256,
    )
    reg_number = models.CharField(
        verbose_name="Регистрационный номер кредитной организации в ЦБ",
        max_length=256,
    )
    internal_number = models.CharField(
        verbose_name="Внутренний номер кредитной организации в ЦБ",
        max_length=256,
    )
    cregnr = models.CharField(
        verbose_name="Дополнительный регистрационный номер в ЦБ",
        max_length=256,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Region(models.Model):
    name = models.CharField(
        verbose_name='Название региона',
        max_length=1000,
    )
    code = models.PositiveSmallIntegerField(
        verbose_name='Код региона',
        unique=True
    )

    def __str__(self):
        return f'{self.code} - {self.name}'

    class Meta:
        ordering = ['name']


class BalanceAccount(models.Model):
    # Например, 202 или 20202
    indCode = models.CharField(
        verbose_name='Номер счета',
        max_length=30,
        unique=True
    )
    name = models.CharField(
        verbose_name='Название счетов баланса',
        max_length=1000,
    )
    # Порядок балансового счета (1 или 2)
    indType = models.CharField(
        verbose_name='Код счета',
        max_length=30,
    )
    # Например, Раздел  - "А"
    indChapter = models.CharField(
        verbose_name='Код раздела',
        max_length=30,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['indCode']
