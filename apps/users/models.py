from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CommunicationNetwork(models.Model):
    name = models.CharField(max_length=128)
    site = models.URLField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', _('user')
        ADMIN = 'admin', _('admin')

    confirmation_code = models.CharField(
        max_length=25,
        editable=True,
        blank=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER)
    is_email_confirmed = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Определяет, подтвердил ли пользователь свой email.'
            'Перешел ли пользователь по ссылке, отправленном в письме.'
        ),
    )
    phone = models.CharField(
        max_length=25,
        blank=True)
    communications = (models.ManyToManyField(CommunicationNetwork,
                      through='UserCommunicationNetwork',
                      through_fields=('user',
                                      'communication_network'),
                      blank=True))

    def __str__(self):
        return f'{self.username}: {self.full_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} '

    class Meta:
        ordering = ['-pk']


class UserCommunicationNetwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    communication_network = models.ForeignKey(CommunicationNetwork,
                                              on_delete=models.CASCADE)
    account = models.CharField(max_length=128)
