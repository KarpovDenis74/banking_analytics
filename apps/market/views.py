from django.shortcuts import render
import requests


class KE:
    def index(self, request):
        url = 'http://kazanexpress.ru'
        response = requests.get(url)
        context = {}
        context['text'] = response.text
        context['meta_description'] = 'Данные с площадки KE'
        context['title'] = 'Данные с площадки KE'
        return render(request, 'market/ke_index.html', context=context)
