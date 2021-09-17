from django.urls import path

from currency.views import CurrencyMode

app_name = 'currency'

urlpatterns = [
    path('<int:cur_day>/',
         CurrencyMode.get_currency_for_day,
         name='currency_for_day'),
]
