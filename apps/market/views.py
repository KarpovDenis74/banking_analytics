from django.shortcuts import render
import requests

# Create your views here.

class KE:
    def index(self, request):
        header = ''
        url = 'http://kazanexpress.ru'
        response = requests.get(url)
        context = {}
        context['text'] = response.text
        context['meta_description'] = 'Данные с площадки KE'
        context['title'] = 'Данные с площадки KE'

        return render(request, 'market/ke_index.html', context=context)