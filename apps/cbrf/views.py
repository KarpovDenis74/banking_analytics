import datetime

import requests


class CBRF:
    """
        Класс для обработки запросов, отправляемых к сайту ЦБ РФ
        Описания API:
            - https://cbr.ru/CreditInfoWebServ/CreditOrgInfo.asmx
            - http://www.cbr.ru/scripts/XML_daily.asp
    """
    """
        свойство methods:
            - справочник методов API ЦБ РФ в формате:
                {название метода: {
                    'endpoint': - точка входа в API для метода
                    'body': - тело запроса для метода
                    'ns': - строка для парсинга ответа
                    'root': - строка для парсинга ответа
                }
    """
    methods = {
        # Справочник курсов валют
        'currency': {
            'endpoint': 'http://www.cbr.ru/scripts/XML_daily.asp',
            'body': '',
            'ns': '',
            'root': ''
        },
        # Справочник индикаторов для формы 101 (как XMLDocument)
        # Список наименования балансовых счетов
        # (см. модель - banks.models.BalanceAccount)
        'Form101IndicatorsEnumXML': {
            'endpoint': 'http://www.cbr.ru/CreditInfoWebServ/'
                        'CreditOrgInfo.asmx',
            'body': ('<?xml version="1.0" encoding="utf-8"?>'
                     '<soap12:Envelope xmlns:xsi='
                     '"http://www.w3.org/2001/XMLSchema-instance" '
                     'xmlns:xsd="http://www.w3.org/2001/XMLSchema" '
                     'xmlns:soap12="http://www.w3.org/2003/05/soap-envelope" >'
                     '<soap12:Body>'
                     '<Form101IndicatorsEnumXML xmlns="http://web.cbr.ru/" />'
                     '</soap12:Body>'
                     '</soap12:Envelope>'
                     ),
            'ns': {'soap': 'http://www.w3.org/2003/05/soap-envelope',
                   '1': 'http://web.cbr.ru/',
                   },
            'root': './soap:Body'
                    '/1:Form101IndicatorsEnumXMLResponse'
                    '/1:Form101IndicatorsEnumXMLResult'
                    '/IndicatorsEnum101'
                    '/EIND'
        },
        # Справочник регионов (как XMLDocument)
        # (см. модель - banks.models.Region )
        'EnumRegions': {
            'endpoint': 'http://www.cbr.ru/CreditInfoWebServ/'
                        'CreditOrgInfo.asmx',
            'body': ('<?xml version="1.0" encoding="utf-8"?>'
                     '<soap12:Envelope xmlns:xsi="http://www.w3.org'
                     '/2001/XMLSchema-instance" xmlns:xsd='
                     '"http://www.w3.org/2001/XMLSchema" xmlns:soap12='
                     '"http://www.w3.org/2003/05/soap-envelope">'
                     '<soap12:Body>'
                     '<EnumRegions xmlns="http://web.cbr.ru/" />'
                     '</soap12:Body>'
                     '</soap12:Envelope>'
                     ),
            'ns': {'soap': 'http://www.w3.org/2003/05/soap-envelope',
                   '1': 'http://web.cbr.ru/',
                   '2': 'urn:schemas-microsoft-com:xml-diffgram-v1',
                   },
            'root': './soap:Body'
                    '/1:EnumRegionsResponse'
                    '/1:EnumRegionsResult'
                    '/2:diffgram'
                    '/EnumRegions'
                    '/ER'
        },
        # Справочник БИК банков (как XMLDocument)
        # (см. модель - banks.models.Bank )
        'EnumBIC': {
            'endpoint': 'http://www.cbr.ru/CreditInfoWebServ/'
                        'CreditOrgInfo.asmx',
            'body': ('<?xml version="1.0" encoding="utf-8"?>'
                     '<soap12:Envelope xmlns:xsi="http://www.w3.org'
                     '/2001/XMLSchema-instance" xmlns:xsd='
                     '"http://www.w3.org/2001/XMLSchema" xmlns:soap12='
                     '"http://www.w3.org/2003/05/soap-envelope" >'
                     '<soap12:Body>'
                     '<EnumBIC xmlns="http://web.cbr.ru/" />'
                     '</soap12:Body>'
                     '</soap12:Envelope>'
                     ),
            'ns': {'soap': 'http://www.w3.org/2003/05/soap-envelope',
                   '1': 'http://web.cbr.ru/',
                   '2': 'urn:schemas-microsoft-com:xml-diffgram-v1',
                   },
            'root': './soap:Body'
                    '/1:EnumBICResponse'
                    '/1:EnumBICResult'
                    '/2:diffgram'
                    '/EnumBIC'
                    '/BIC'
        },
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
            CBRF.methods.get('currency')
            .get('endpoint'), params=params)
        return response

    def query(self, method):
        """
            Метод делает запрос к API ЦБРФ
            в соответсвии с инициализирующим экземпляр класса параметром
            Входящие параметры:
                - method: название метода запроса к API
            Результат функции:
                - возвращает объект response:
                    xml с информацией об обработке инициализирующего метода
        """
        if not(method in CBRF.methods.keys()):
            return None
        body = CBRF.methods.get(method).get('body')
        body = body.encode('utf-8')
        endpoint = CBRF.methods.get(method).get('endpoint')
        session = requests.session()
        session.headers = {"Content-Type": "text/xml; charset=utf-8"}
        session.headers.update({"Content-Length": str(len(body))})
        response = session.post(url=endpoint,
                                data=body,
                                verify=False)
        return response
