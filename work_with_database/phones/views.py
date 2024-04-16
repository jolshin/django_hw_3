from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_ = request.GET.get('sort', 'id')
    if sort_ == 'max_price':
        phones = Phone.objects.order_by('price').reverse()
    elif sort_ == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.order_by(sort_)

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).values().first()
    
    context = {
        'phone': phone
    }
    print(phone)
    return render(request, template, context)
