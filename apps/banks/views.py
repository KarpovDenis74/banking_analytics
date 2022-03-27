import datetime
from pathlib import Path

from django.shortcuts import render

from apps.banks.models import BalanceAccount, Bank, BanksBalance, Region
from apps.cbrf.views import CBRF


class BankView:
    def view_bic(request):
        banks = Bank.objects.all()
        context = {
            'title': 'Кредитные организации',
            'header': 'Банки',
            'banks': banks,
        }
        return render(request, 'banks/banks.html', context)

    def view_regions(request):
        regions = Region.objects.all()
        context = {
            'title': 'Регионы',
            'header': 'Список регионов',
            'regions': regions,
        }
        return render(request, 'banks/get_regions.html', context)

    def view_accounts(request):
        accounts = BalanceAccount.objects.all()
        context = {
            'title': 'Справочник балансовых счетов кредитных организаций',
            'header': 'Справочник балансовых счетов',
            'accounts': accounts,
        }
        return render(request, 'banks/accounts.html', context)

    def view_balance(request, id_bank):
        bank = Bank.objects.get(pk=id_bank)
        balances = BanksBalance.objects.filter(bank=bank)
        context = {
            'title': f'Баланс кредитной организации {bank.short_name}',
            'header': 'Справочник балансовых счетов',
            'balances': balances,
        }
        return render(request, 'banks/balance.html', context)

    def view_101(request):
        cb = CBRF()
        response = cb.query(method='Data101FullV2XML')
        data_directory = Path('apps/banks/cbr_data/Data101FullV2XML')
        now_date = datetime.date.today()
        data_file = Path(f'{now_date.strftime("%Y_%m_%d")}.xml')
        file_name = data_directory / data_file
        with open(file_name, 'w+', encoding="utf-8") as file:
            file.write(response.text)
