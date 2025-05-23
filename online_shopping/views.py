from django.shortcuts import render, redirect
from online_electronic_shopping.models import Product, Categories, Filter_Price, Color, Brand, contant_us
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


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


def REGISTER(request):
    if request.method=="POST":
        username= request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        customer= User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name

        customer.save()
        return redirect('register')
    return render(request,'registration/auth.html')


def LOGIN(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')


    return render(request,'registration/auth.html')


def LOGOUT(request):
    logout(request)


    return redirect('home')


#def CARD(request):

 #   return render(request, 'card/card_detail.html')


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'card/card_detail.html')


def CHECKOUT(request):

    return render(request,'card/checkout.html')