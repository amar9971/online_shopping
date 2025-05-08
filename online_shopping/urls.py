
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

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

