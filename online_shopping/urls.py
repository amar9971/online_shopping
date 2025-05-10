
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.BASE,name='base'),
    path('products/', views.PRODUCT,name='product'),
    path('search/', views.SEARCH,name='search'),
    path('product_details/<str:id>', views.PRODUCT_DETAILS, name='product_details'),
    path('contact_us/', views.CONTACT_US, name='contact_us'),
    path('register/', views.REGISTER, name='register'),
    path('login/', views.LOGIN, name='login'),
    path('logout/', views.LOGOUT, name='logout'),
    #path('card/card_details/', views.CARD, name='card_detail'),

    #card
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('card/checkout/', views.CHECKOUT, name='checkout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

