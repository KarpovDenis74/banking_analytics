from django.shortcuts import render

from apps.banks.models import BalanceAccount, Bank, Region


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
