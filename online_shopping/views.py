from django.shortcuts import render, redirect
from online_electronic_shopping.models import Product, Categories, Filter_Price, Color,Brand


def BASE(request):
    return render(request, 'main/base.html')


def home(request):
    product = Product.objects.filter(status = 'Publish' )

    cantext = {
        'product': product,
    }

    return render(request, 'main/index.html', cantext)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    filter_price= Filter_Price.objects.all()
    color = Color.objects.all()
    brand= Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID= request.GET.get('filter_Price')
    COLOR_ID= request.GET.get('Color')
    BRAND_ID= request.GET.get('brand')

    if CATID:
        product= Product.objects.filter(Categories=CATID,status='Publish')

    elif PRICE_FILTER_ID:
        product= Product.objects.filter(Filter_Price='PRICE_FILTER_ID',status='Publish')
    elif COLOR_ID:
        product= Product.objects.filter(Color='COLOR_ID',status='Publish')

    elif BRAND_ID:
        product=Product.objects.filter(Brand='BRAND_ID',status='Publish')

    else:
        product= Product.objects.filter(status='Publish')

    cantext = {
        'product': product,
        'categories':categories,
        'filter_price': filter_price,
        'color': color,
        'brand':brand,

    }
    return render(request,'main/product.html',cantext)