# from django.core.paginator import Paginator
from django.shortcuts import render

from apps.news.models import News


class NewsView:
    def index(request):
        news = News.objects.all()
        context = {
            'title': 'Новости',
            'header': 'Новости',
            'news': news,
        }
        return render(request, 'news/news.html', context)

    def detail(request, pk):
        news = News.objects.get(id=pk)
        context = {
            'title': 'Новости',
            'header': 'Новости',
            'news': news,
        }
        return render(request, 'news/news.html', context)
