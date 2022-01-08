# from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.base import TemplateView

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


class AuthorPage(TemplateView):
    template_name = 'banks/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        return context


class TeсhnologiesPage(TemplateView):
    template_name = 'banks/teсhnologies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Используемые технологии'
        return context


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)
