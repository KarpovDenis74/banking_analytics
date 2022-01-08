import datetime
import xml.etree.ElementTree as ET
from pathlib import Path

from banking_analytics.celery import app

from apps.banks.models import Bank, Region, BalanceAccount
from apps.cbrf.views import CBRF


@app.task
def get_accounts():
    cb = CBRF()
    response = cb.query(method='Form101IndicatorsEnumXML')
    data_directory = Path('apps/banks/cbr_data/Form101IndicatorsEnum')
    now_date = datetime.date.today()
    data_file = Path(f'{now_date.strftime("%Y_%m_%d")}.xml')
    file_name = data_directory / data_file
    with open(file_name, 'w+', encoding="utf-8") as file:
        file.write(response.text)
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    ns = cb.methods.get('Form101IndicatorsEnumXML').get('ns')
    root = tree.findall(
        cb.methods.get('Form101IndicatorsEnumXML').get('root'), ns)
    for child in root:
        indCode = str(child.find('IndCode').text)
        name = str(child.find('name').text)
        indType = str(child.find('IndType').text)
        indChapter = str(child.find('IndChapter').text)
        bank, _ = BalanceAccount.objects.get_or_create(
            indCode=indCode,
            defaults={'name': name,
                      'indType': indType,
                      'indChapter': indChapter,
                      }
        )
    file_name.unlink(missing_ok=False)
    return 'OK'


@app.task
def get_regions():
    cb = CBRF()
    response = cb.query(method='EnumRegions')
    data_directory = Path('apps/banks/cbr_data/EnumRegions')
    now_date = datetime.date.today()
    data_file = Path(f'{now_date.strftime("%Y_%m_%d")}.xml')
    file_name = data_directory / data_file
    with open(file_name, 'w+', encoding="utf-8") as file:
        file.write(response.text)
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    ns = cb.methods.get('EnumRegions').get('ns')
    root = tree.findall(
        cb.methods.get('EnumRegions').get('root'), ns)
    for child in root:
        name = str(child.find('Name').text)
        code = int(child.find('rgn').text)
        region, _ = Region.objects.get_or_create(
            code=code,
            defaults={'name': name}
        )
    file_name.unlink(missing_ok=False)
    return 'OK'


@app.task
def get_bics():
    cb = CBRF()
    response = cb.query(method='EnumBIC')
    data_directory = Path('apps/banks/cbr_data/EnumBIC')
    now_date = datetime.date.today()
    data_file = Path(f'{now_date.strftime("%Y_%m_%d")}.xml')
    file_name = data_directory / data_file
    with open(file_name, 'w+', encoding="utf-8") as file:
        file.write(response.text)
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser=parser)
    ns = cb.methods.get('EnumBIC').get('ns')
    root = tree.findall(
        cb.methods.get('EnumBIC').get('root'), ns)
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
    file_name.unlink(missing_ok=False)
    return 'OK'
