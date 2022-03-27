from statistics import mode
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.deletion import CASCADE


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


class BanksBalance(models.Model):
    date = models.DateField(
        verbose_name="Балансовые данные на дату",
    )
    bank = models.ForeignKey(Bank,
        verbose_name="Банк",
        on_delete=CASCADE,
        blank=False,
    )
    # Например, 202 или 20202
    indCode = models.ForeignKey(BalanceAccount,
        verbose_name="Номер счета",
        on_delete=CASCADE,
        blank=False,
    )
    rub_balance = models.IntegerField(
        verbose_name='Остаток в рублях на дату',
    )
    cur_balance = models.IntegerField(
        verbose_name='Остаток в валюте на дату',
    )
    itog_balance = models.IntegerField(
        verbose_name='Итоговый остаток в рублях и в валюте на дату',
    )
    ora = models.IntegerField(
        verbose_name='Оборот в рублях по дебиту',
    )
    ova = models.IntegerField(
        verbose_name='Оборот в валюте по дебиту',
    )
    oitga = models.IntegerField(
        verbose_name='Итоговый оборот в рублях и в валюте по дебету',
    )
    orp = models.IntegerField(
        verbose_name='Оборот в рублях по кредиту',
    )
    ovp = models.IntegerField(
        verbose_name='Оборот в валюте по кредиту',
    )
    oitgp = models.IntegerField(
        verbose_name='Итоговый оборот в рублях и в валюте по кредиту',
    )

    def __str__(self):
        return f'{self.value} :  {self.indCode}     {self.itog_balance}'

    class Meta:
        UniqueConstraint(fields=['date', 'indCode', 'bank'],
                         name='unique_date_indCode_bank')
        verbose_name = 'Остатки на дату и обороты за предыдущий период'
        verbose_name_plural = 'Остатки на дату и обороты за предыдущий период'
        ordering = ['-date']
