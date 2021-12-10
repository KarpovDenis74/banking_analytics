from django.urls import path

from apps.core.views import CoreView

app_name = 'core'

urlpatterns = [path('', CoreView.index, name='index'), ]
