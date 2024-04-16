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
    elif sort_ == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()

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
