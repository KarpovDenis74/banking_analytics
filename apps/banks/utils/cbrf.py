import requests
import datetime


class CBRF_query:
    endpoint = 'http://www.cbr.ru/CreditInfoWebServ/CreditOrgInfo.asmx'
    dirs = {
        'EnumBIC': 'apps/banks/cbr_data/EnumBIC',
        'EnumRegions': 'apps/banks/cbr_data/EnumRegions',
    }
    body = {
        'EnumRegions': ('<?xml version="1.0" encoding="utf-8"?>'
                        '<soap12:Envelope xmlns:xsi="http://www.w3.org'
                        '/2001/XMLSchema-instance" xmlns:xsd='
                        '"http://www.w3.org/2001/XMLSchema" xmlns:soap12='
                        '"http://www.w3.org/2003/05/soap-envelope">'
                        '<soap12:Body>'
                        '<EnumRegions xmlns="http://web.cbr.ru/" />'
                        '</soap12:Body>'
                        '</soap12:Envelope>'
                        ),
        'EnumBIC': ('<?xml version="1.0" encoding="utf-8"?>'
                    '<soap12:Envelope xmlns:xsi="http://www.w3.org'
                    '/2001/XMLSchema-instance" xmlns:xsd='
                    '"http://www.w3.org/2001/XMLSchema" xmlns:soap12='
                    '"http://www.w3.org/2003/05/soap-envelope" >'
                    '<soap12:Body>'
                    '<EnumBIC xmlns="http://web.cbr.ru/" />'
                    '</soap12:Body>'
                    '</soap12:Envelope>'
                    ),
    }

    def _save_to_file(method, data):
        now_date = datetime.date.today()
        file_name = (f'{CBRF_query.dirs.get(method)}/'
                     f'{now_date.strftime("%Y_%m_%d")}_{method}.xml')
        with open(file_name, 'w+', encoding="utf-8") as file:
            file.write(data)
        return file_name

    def query(method):
        body = CBRF_query.body.get(method)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = {"Content-Type": "text/xml; charset=utf-8"}
        session.headers.update({"Content-Length": str(len(body))})
        response = session.post(url=CBRF_query.endpoint,
                                data=body,
                                verify=False)
        file_name = CBRF_query._save_to_file(
            method, response.content.decode('utf-8'))
        return file_name
