from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import CurrencyAPI

router = DefaultRouter()
# возвращает курсы валют за определенную дату
# дата в формате  31-09-2021
# пример запроса:
# /api/v1/currency/17-09-2021/
router.register(r'currency/(?P<cur_day>\d+[-]\d+[-]\d+)',
                CurrencyAPI,
                basename='currency') 

urlpatterns = [
    path('v1/', include(router.urls)),
]
