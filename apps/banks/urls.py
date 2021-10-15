from django.urls import path

from apps.banks import views

app_name = 'banks'

urlpatterns = [
    path('', views.BankView.index, name='index'),
    path('regions/', views.CBRF.get_regions, name='get_regions'),
    path('bic-list/', views.CBRF.get_enum_bic, name='get_enum_bic'),
]
