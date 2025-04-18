
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

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

