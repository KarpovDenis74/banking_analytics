from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bank(models.Model):
    long_name = models.CharField(
        verbose_name="Польное наименование",
        max_length=256,
    )
    sort_name = models.CharField(
        verbose_name="Cjrращенное наименование",
        max_length=256,
    )

    def __str__(self):
        return self.sort_name

    class Meta:
        ordering = ['sort_name']
