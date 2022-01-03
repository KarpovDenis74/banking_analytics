from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.banks.models import Bank, Region
from apps.banks.tasks import set_bics, set_regions
from apps.banks.utils.cbrf import CBRF_query


class BankView:
    def index(request):
        banks = Bank.objects.all()
        context = {
            'title': 'Кредитные организации',
            'header': 'Банки',
            'banks': banks,
        }
        return render(request, 'banks/banks.html', context)

    def view_regions(request):
        regions = Region.objects.all()
        context = {
            'title': 'Регионы',
            'header': 'Список регионов',
            'regions': regions,
        }
        return render(request, 'banks/get_regions.html', context)


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

    def get_form_101(request):
        file_name = CBRF_query.query('Data101FullV2XML')
        return render(request, file_name)
        # parser = ET.XMLParser(encoding="utf-8")
        # tree = ET.parse(file_name, parser=parser)
        # ns = {
        #     'soap': 'http://www.w3.org/2003/05/soap-envelope',
        #     '1': 'http://web.cbr.ru/',
        #     '2': 'urn:schemas-microsoft-com:xml-diffgram-v1',
        # }
        # root = tree.findall(
        #     './soap:Body'
        #     '/1:EnumBICResponse'
        #     '/1:EnumBICResult'
        #     '/2:diffgram'
        #     '/EnumBIC'
        #     '/BIC', ns)
        # for child in root:
        #     bic = str(child.find('BIC').text)
        #     reg_date = str(child.find('RC').text)
        #     reg_date = datetime.datetime.strptime(
        #         reg_date, '%Y-%m-%dT%H:%M:%S%z').date()
        #     name = str(child.find('NM').text)
        #     ogrn = str(child.find('RB').text)
        #     cregnr = str(child.find('cregnr').text)
        #     internal_number = str(child.find('intCode').text)
        #     reg_number = str(child.find('RN').text)
        #     bank, _ = Bank.objects.get_or_create(
        #         ogrn=ogrn,
        #         defaults={'bic': bic,
        #                 'reg_date': reg_date,
        #                 'name': name,
        #                 'cregnr': cregnr,
        #                 'internal_number': internal_number,
        #                 'reg_number': reg_number,
        #                 }
        #     )


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
