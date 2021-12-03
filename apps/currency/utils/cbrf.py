import requests
import datetime


class CBRF_query_currency:
    endpoint = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dirs = {
        'currency': 'apps/currency/cbr_data/currency',
    }

    def get_file_currency() -> str:
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
        params = {'date_req': now_date_string}
        response = requests.get(
            CBRF_query_currency.endpoint, params=params)
        file_name = (f'{CBRF_query_currency.dirs.get("currency")}/'
                     f'{now_date.strftime("%Y_%m_%d")}.xml')
        with open(file_name, 'w+', encoding="utf-8") as file:
            file.write(response.text)
        return file_name
