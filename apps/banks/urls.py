from django.urls import path

from apps.banks.views import BankView
from apps.banks.tasks import (get_regions, get_accounts, get_bics)

app_name = 'banks'

urlpatterns = [
    # отображение справочников
    path('', BankView.view_bic, name='view_bic'),
    path('view_regions/', BankView.view_regions, name='view_regions'),
    path('view_accounts/', BankView.view_accounts, name='view_accounts'),
    # Запросы к API ЦБ РФ
    path('get_regions/', get_regions, name='get_regions'),
    path('get_accounts/', get_accounts, name='get_accounts'),
    path('get_bics/', get_bics, name='get_bics'),

]
