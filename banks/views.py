import datetime
import xml.etree.ElementTree as ET

import requests
from currency.models import CurrencyRate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView

from banks.models import Bank


class BanksView:
    def index(request):
        currency = CurrencyRate.objects.filter(date=datetime.date.today())
        context = {
            'currency': currency,
        }
        return render(request, 'banks/index.html', context)


class AuthorPage(TemplateView):
    template_name = 'banks/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        return context


class TeсhnologiesPage(TemplateView):
    template_name = 'banks/teсhnologies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Используемые технологии'
        return context


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )

def server_error(request):
    return render(request, "misc/500.html", status=500)
