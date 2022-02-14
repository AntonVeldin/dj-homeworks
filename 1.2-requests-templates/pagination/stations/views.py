from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    all_bus_stations = []
    with open(BUS_STATION_CSV) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            station = {}
            station['Name'] = row['Name']
            station['Street'] = row['Street']
            station['District'] = row['District']
            all_bus_stations.append(station)

    paginator = Paginator(all_bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
