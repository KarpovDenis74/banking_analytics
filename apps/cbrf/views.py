import requests
import datetime


class CBRF_query:
    """
        Класс для обработки запросов, отправляемых  к сайту ЦБ РФ

    """
    endpoint = {
        'currency': 'http://www.cbr.ru/scripts/XML_daily.asp',
        'CreditOrgInfo': 'http://www.cbr.ru/CreditInfoWebServ/'
                         'CreditOrgInfo.asmx',
    }

    def get_currency_today():
        """
            Метод делает запрос к API ЦБРФ
            для получения курсов валют за текущую дату.
            Результат функции:
                1. возвращает объект response:
                    xml с информацией о текущем курсе валют
        """
        now_date = datetime.date.today()
        now_date_string = now_date.strftime('%d/%m/%Y')
        params = {'date_req': now_date_string}
        response = requests.get(
            CBRF_query.endpoint.get('currency'), params=params)
        return response
