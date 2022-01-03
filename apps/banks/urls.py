from django.urls import path

from apps.banks.views import BankView, CBRF

app_name = 'banks'

urlpatterns = [
    path('', BankView.index, name='index'),
    path('view_regions/', BankView.view_regions, name='view_regions'),
    path('regions/', CBRF.get_regions, name='get_regions'),
    path('bic-list/', CBRF.get_enum_bic, name='get_enum_bic'),
    path('get_form_101/', CBRF.get_form_101, name='get_form_101'),
]
