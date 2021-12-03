import datetime
import xml.etree.ElementTree as ET

import requests
from django.conf import settings
# from django.core.paginator import Paginator
from django.shortcuts import render

from apps.currency.models import Currency, CurrencyRate
from apps.currency import tasks


class CurrencyMode:
    def get_currency_for_day(request):
        tasks.set_currency.delay()
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
