from django.urls import path

from apps.banks.views import BankView

app_name = 'banks'

urlpatterns = [
    # отображение справочников
    path('', BankView.view_bic, name='view_bic'),
    path('view_regions/', BankView.view_regions, name='view_regions'),
    path('view_accounts/', BankView.view_accounts, name='view_accounts'),
    # Запросы к API ЦБ РФ

]
