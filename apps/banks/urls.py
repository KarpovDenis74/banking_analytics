from django.urls import path

from apps.banks import views

app_name = 'banks'

urlpatterns = [
    path('', views.BankView.index, name='index'),
]
