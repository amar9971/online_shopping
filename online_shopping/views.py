from django.shortcuts import render, redirect
from online_electronic_shopping.models import Product


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

    cantext = {
        'product': product,
    }
    return render(request,'main/product.html',cantext)