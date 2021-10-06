from django.urls import path

from apps.currency.views import CurrencyMode, CurrencyView

app_name = 'currency'

urlpatterns = [
    path('',
         CurrencyView.index,
         name='index'),
    path('request_courses/',
         CurrencyMode.get_currency_for_day,
         name='get_currency_for_day'),
    path('example/',
         CurrencyView.example,
         name='example'),
]
