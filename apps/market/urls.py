from django.urls import path
from apps.market.views import KE

app_name = 'market'
ke = KE()

urlpatterns = [path('ke/', ke.index, name='ke'), ]
