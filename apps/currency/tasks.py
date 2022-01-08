import datetime
import xml.etree.ElementTree as ET
from pathlib import Path

from banking_analytics.celery import app

from apps.cbrf.views import CBRF
from apps.currency.models import Currency, CurrencyRate


@app.task
def get_currency():
    data_directory = Path('apps/currency/cbr_data/currency')
    now_date = datetime.date.today()
    data_file = Path(f'{now_date.strftime("%Y_%m_%d")}.xml')
    currency_query = CBRF.get_currency_today()
    file_name = data_directory / data_file
    with open(file_name, 'w+', encoding="utf-8") as file:
        file.write(currency_query.text)
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
    file_name.unlink(missing_ok=False)
    return 'OK'
