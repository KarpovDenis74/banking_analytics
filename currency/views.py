import datetime
import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from currency.models import Currency, CurrencyRate


class CurrencyMode:
    url_currency = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dirs = {
        'currency': 'currency/cbr_data/currency',
    }

    def __get_file_currency() -> str:
        """
            Внутренний метод делает запрос к API ЦБРФ
            для получения курсов валют за текущую дату.
            Результат функции:
                1. запись в файл полученных данных
                в формате XML
                2. возвращает имя созданного файла
        """
        now_date = datetime.date.today()
        now_date_string = now_date.strftime('%d/%m/%Y')
        print(f'Текущая дата: {now_date_string}')
        params = {'date_req': now_date_string}
        response = requests.get(CurrencyMode.url_currency, params=params)
        file_name = (f'{CurrencyMode.dirs["currency"]}/'
                     f'{now_date.strftime("%Y_%m_%d")}.currency')
        with open(file_name, 'w+', encoding="utf-8") as file:
            file.write(response.text)
        return file_name

    def get_currency_for_day(request):
        file_name = CurrencyMode.__get_file_currency()
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(file_name, parser=parser)
        root = tree.getroot()
        date_rate_str = str(root.attrib.get('Date'))  # Date="31.08.2021"
        date_rate = datetime.datetime.strptime(date_rate_str, "%d.%m.%Y")
        print(date_rate)
        for child in root.findall('Valute'):
            num_code = int(child.find('NumCode').text)
            char_code = str(child.find('CharCode').text)
            name = str(child.find('Name').text)
            currency, _ = Currency.objects.get_or_create(
                num_code=num_code,
                defaults={'char_code': char_code,
                          'name': name},
            )
            value = float(child.find('Value').text.replace(',', '.'))
            nominal = int(child.find('Nominal').text)
            currency_rate, _ = CurrencyRate.objects.get_or_create(
                date=date_rate,
                currency=currency,
                value=value,
                nominal=nominal
            )
        currency = CurrencyRate.objects.filter(date=date_rate)
        context = {
            'currency': currency,
            'date_rate_str': date_rate_str,
        }
        return render(request, 'currency/get_currency_for_day.html', context)


class CurrencyView:
    def index(request):
        currency_rate = (CurrencyRate.objects.filter(
            date=datetime.date.today())
            .select_related('currency')
        )
        currency = (Currency.objects.all(
            )[:settings.REST_FRAMEWORK.get('PAGE_SIZE')]
        )

        context = {
            'title': 'Курсы валют',
            'header': 'Курсы валют',
            'currency': currency,
            'currency_rate': currency_rate,
        }
        return render(request, 'currency/currency.html', context)

    def example(request):
        return render(request, 'currency/_example.html')
