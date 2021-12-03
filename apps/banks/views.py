import datetime
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.banks.models import Bank, Region
from apps.banks.utils.cbrf import CBRF_query

from apps.banks.tasks import set_regions, set_bics


class BankView:
    def index(request):
        context = {
            'title': 'Кредитные организации',
            'header': 'Банки',
        }
        return render(request, 'banks/banks.html', context)


class CBRF:
    def get_regions(request):
        set_regions.delay()
        regions = Region.objects.all()
        context = {
            'title': 'Регионы',
            'header': 'Список регионов',
            'regions': regions,
        }
        return render(request, 'banks/get_regions.html', context)

    def get_enum_bic(request):
        set_bics.delay()
        banks = Bank.objects.all()

        context = {
            'title': 'Список БИК кредитных организаций',
            'header': 'Список БИК кредитных организаций',
            'banks': banks,
        }
        return render(request, 'banks/get_bic.html', context)


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
