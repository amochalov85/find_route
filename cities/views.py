from django.shortcuts import render

from cities.models import City

__all__ = (
    'home',
)

# функция отображения городов
# получение списка всех городов и передача в контекстное меню
# context - словарь со списком городов


def home(request):
    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)
