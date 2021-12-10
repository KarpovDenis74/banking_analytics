from datetime import date
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):

    def get_image_path(self, filename):
        filename = filename.strip()
        date_today = date.today()
        year = date_today.strftime("%Y")
        month = date_today.strftime("%m")
        directory = (Path(settings.MEDIA_ROOT)
                     .joinpath(Path('news'))
                     .joinpath(Path(year))
                     .joinpath(Path(month))
                     )
        if not directory.exists():
            directory.mkdir(parents=True)
        return (Path('news')
                .joinpath(Path(year))
                .joinpath(Path(month))
                .joinpath(Path(filename)))

    title = models.CharField(
        blank=False,
        verbose_name="Заголовок новости",
        max_length=128,
    )
    text = models.CharField(
        blank=False,
        verbose_name="Текст новости",
        max_length=2000,
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Публикуемая новость ?",
    )
    data_news = models.DateTimeField(
        verbose_name="Дата создания новости",
        auto_now_add=True,
    )
    update_news = models.DateTimeField(
        verbose_name="Дата последнего изменения новости",
        auto_now=True,
    )
    image = models.ImageField(upload_to=get_image_path,
                              verbose_name='Фото для новости',
                              )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_news']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
