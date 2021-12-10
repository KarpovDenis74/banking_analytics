# from django.core.paginator import Paginator
from django.shortcuts import render

from apps.news.models import News


class CoreView:
    def index(request):
        news = News.objects.all()[:5]
        context = {
            'title': 'Актуальные данные по темам',
            'header': 'Банковская аналитика',
            'news': news,
        }
        return render(request, 'core/core.html', context)
