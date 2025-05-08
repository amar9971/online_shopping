from django.shortcuts import render, redirect
from online_electronic_shopping.models import Product, Categories, Filter_Price, Color, Brand, contant_us
from django.conf import settings
from django.core.mail import send_mail


def BASE(request):
    return render(request, 'main/base.html')


def home(request):
    product = Product.objects.filter(status='Publish')

    cantext = {
        'product': product,
    }

    return render(request, 'main/index.html', cantext)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_Price')
    COLOR_ID = request.GET.get('Color')
    BRAND_ID = request.GET.get('brand')

    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LOWTOHIGH = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOW = request.GET.get('PRICE_HIGHTOLOW')

    NEW_PRODUCT = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCT = request.GET.get('OLD_PRODUCT')

    if CATID:
        product = Product.objects.filter(Categories=CATID, status='Publish')

    elif PRICE_FILTER_ID:
        product = Product.objects.filter(Filter_Price='PRICE_FILTER_ID', status='Publish')
    elif COLOR_ID:
        product = Product.objects.filter(Color='COLOR_ID', status='Publish')

    elif BRAND_ID:
        product = Product.objects.filter(Brand='BRAND_ID', status='Publish')

    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')

    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')

    elif PRICE_LOWTOHIGH:
        product = Product.objects.filter(status='Publish').order_by('price')

    elif PRICE_HIGHTOLOW:
        product = Product.objects.filter(status='Publish').order_by('-price')

    elif NEW_PRODUCT:
        product = Product.objects.filter(status='Publish', condition='New').order_by('-id')

    elif OLD_PRODUCT:
        product = Product.objects.filter(status='Publish', condition='Old').order_by('-id')

    else:
        product = Product.objects.filter(status='Publish').order_by('-id')

    cantext = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,

    }
    return render(request, 'main/product.html', cantext)


def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)

    context = {
        'product': product,
    }

    return render(request, "main/search.html", context)


def PRODUCT_DETAILS(request, id):
    prod = Product.objects.filter(id=id).first()
    context = {
        'prod': prod,
    }
    return render(request, 'main/singleproduct.html', context)


def CONTACT_US(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        massege = request.POST.get('massege')

        contact = contant_us(
            name=name,
            email=email,
            subject=subject,
            massege=massege
        )
        # contact.save()
        # return redirect('home')
        subject = subject
        massege = massege
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, massege, email_from, ['write your email'])
            contact.save()
            return redirect('home')
        except:

            return redirect('contact_us')

    return render(request, 'main/contact.html')
