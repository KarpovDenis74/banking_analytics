import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.currency.models import Currency, CurrencyRate


class BankView:
    def index(request):
        rate_date = datetime.date.today().strftime("%Y-%m-%d")
        currency_rate = (CurrencyRate.objects.filter(
            date=datetime.date.today())
            .select_related('currency')
        )
        currency = (Currency.objects
                    .all()[:settings.REST_FRAMEWORK.get('PAGE_SIZE')])
        context = {
            'title': 'Кредитные организации',
            'header': 'Банки',
            'currency': currency,
            'rate_date': rate_date,
            'currency_rate': currency_rate,
        }
        return render(request, 'banks/banks.html', context)


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
