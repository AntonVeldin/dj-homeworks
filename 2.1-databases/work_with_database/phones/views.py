from django.shortcuts import render, redirect
from phones.models import Phone

SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price'
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort:
        phones = Phone.objects.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
