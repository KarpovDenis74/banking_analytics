from django.urls import path

from apps.news.views import NewsView

app_name = 'news'

urlpatterns = [path('', NewsView.index, name='index'),
               path('detail/<int:news_id>/', NewsView.detail, name='detail'),
               ]
