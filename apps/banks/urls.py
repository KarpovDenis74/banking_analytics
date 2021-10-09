from django.urls import path

from apps.banks import views
from apps.currency.views import CurrencyView

app_name = 'banks'

urlpatterns = [
    path('', views.BankView.index, name='index'),
]
