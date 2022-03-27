from django.urls import path

from apps.banks.tasks import get_accounts, get_bics, get_regions
from apps.banks.views import BankView

app_name = 'banks'

urlpatterns = [
    # отображение справочников
    path('', BankView.view_bic, name='view_bic'),
    path('view_regions/', BankView.view_regions, name='view_regions'),
    path('view_accounts/', BankView.view_accounts, name='view_accounts'),
    path('view_101/', BankView.view_101, name='view_101'),
    # Запросы к API ЦБ РФ
    path('get_regions/', get_regions, name='get_regions'),
    path('get_accounts/', get_accounts, name='get_accounts'),
    path('view_balance/<int:id_bank>/',
         BankView.view_balance, name='view_balance'),
    path('get_bics/', get_bics, name='get_bics'),
]
