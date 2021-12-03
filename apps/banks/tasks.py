import datetime
import xml.etree.ElementTree as ET

from banking_analytics.celery import app

from apps.banks.models import Bank, Region
from apps.banks.utils.cbrf import CBRF_query


@app.task
def set_regions():
    file_name = CBRF_query.query('EnumRegions')
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    ns = {
        'soap': 'http://www.w3.org/2003/05/soap-envelope',
        '1': 'http://web.cbr.ru/',
        '2': 'urn:schemas-microsoft-com:xml-diffgram-v1',
    }
    root = tree.findall(
        './soap:Body'
        '/1:EnumRegionsResponse'
        '/1:EnumRegionsResult'
        '/2:diffgram'
        '/EnumRegions'
        '/ER',
        ns)
    for child in root:
        name = str(child.find('Name').text)
        code = int(child.find('rgn').text)
        region, _ = Region.objects.get_or_create(
            code=code,
            defaults={'name': name}
        )


@app.task
def set_bics():
    file_name = CBRF_query.query('EnumBIC')
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    ns = {
        'soap': 'http://www.w3.org/2003/05/soap-envelope',
        '1': 'http://web.cbr.ru/',
        '2': 'urn:schemas-microsoft-com:xml-diffgram-v1',
    }
    root = tree.findall(
        './soap:Body'
        '/1:EnumBICResponse'
        '/1:EnumBICResult'
        '/2:diffgram'
        '/EnumBIC'
        '/BIC', ns)
    for child in root:
        bic = str(child.find('BIC').text)
        reg_date = str(child.find('RC').text)
        reg_date = datetime.datetime.strptime(
            reg_date, '%Y-%m-%dT%H:%M:%S%z').date()
        name = str(child.find('NM').text)
        ogrn = str(child.find('RB').text)
        cregnr = str(child.find('cregnr').text)
        internal_number = str(child.find('intCode').text)
        reg_number = str(child.find('RN').text)
        bank, _ = Bank.objects.get_or_create(
            ogrn=ogrn,
            defaults={'bic': bic,
                      'reg_date': reg_date,
                      'name': name,
                      'cregnr': cregnr,
                      'internal_number': internal_number,
                      'reg_number': reg_number,
                      }
        )
