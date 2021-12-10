from django.contrib import admin

from apps.news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'is_public', 'image',)
    search_fields = ('title',)
    list_filter = ('is_public', 'update_news', 'data_news')
    empty_value_display = "-пусто-"


admin.site.register(News, NewsAdmin)
