import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from apps.currency import tasks
from apps.currency.models import Currency, CurrencyRate


class CurrencyMode:
    @login_required()
    def get_currency_for_day(request):
        if not request.user.is_staff:
            return redirect('core:index')
        tasks.get_currency.delay()
        context = {}
        return render(request, 'currency/get_currency_for_day.html', context)


class CurrencyView:
    def index(request):
        rate_date = datetime.date.today().strftime("%Y-%m-%d")
        currency_rate = (CurrencyRate.objects.filter(
            date=datetime.date.today())
            .select_related('currency')
        )
        currency = (Currency.objects
                    .all()[:settings.REST_FRAMEWORK.get('PAGE_SIZE')])
        context = {
            'rate_date': rate_date,
            'title': 'Курсы валют',
            'header': 'Курсы валют',
            'currency': currency,
            'currency_rate': currency_rate,
        }
        return render(request, 'currency/currency.html', context)

    def example(request):
        return render(request, 'apps/currency/_example.html')
