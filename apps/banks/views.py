import datetime

from apps.currency.models import CurrencyRate
from django.shortcuts import render
from django.views.generic.base import TemplateView


class BanksView:
    def index(request):
        currency = CurrencyRate.objects.filter(date=datetime.date.today())
        context = {
            'currency': currency,
        }
        return render(request, 'banks/index.html', context)


class AuthorPage(TemplateView):
    template_name = 'apps/banks/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        return context


class TeсhnologiesPage(TemplateView):
    template_name = 'apps/banks/teсhnologies.html'

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
