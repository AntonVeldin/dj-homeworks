import datetime
import os

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, reverse


# region home_view
def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Пагинатор': reverse('my_pagi')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
# endregion


# region base_views
def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_in_workdir = os.listdir('.')
    msg = ', '.join(files_in_workdir)
    return HttpResponse(msg)
# endregion


# region paginator
CONTENT = [str(i) for i in range(10000)]


def my_pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'my_pagi.html', context)
# endregion


# region custom_path_converter
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> datetime:
       return datetime.datetime.strptime(value, self.format)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)


from django.urls import register_converter

register_converter(DateConverter, 'date')


def user_report(request, dt: datetime):
    msg = f'lalala {dt}'
    return HttpResponse(msg)
# endregion


# region html_render
def hello(request):
    context = {
        'test': 5,
        'data': [1, 5, 8],
    }
    return render(request, 'demo.html', context)

# endregion
