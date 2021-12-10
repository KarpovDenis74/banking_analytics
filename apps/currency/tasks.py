import datetime
import xml.etree.ElementTree as ET

from banking_analytics.celery import app

from apps.currency.models import Currency, CurrencyRate
from apps.currency.utils.cbrf import CBRF_query_currency


@app.task
def set_currency():
    print('set_currency  - begined')
    file_name = CBRF_query_currency.get_file_currency()
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    root = tree.getroot()
    date_rate_str = str(root.attrib.get('Date'))  # Date="31.08.2021"
    date_rate = datetime.datetime.strptime(date_rate_str, "%d.%m.%Y")
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
    print('set_currency  - ended')
