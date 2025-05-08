from django.contrib import admin
from .models import *
# Register your models here.
class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag

class Productadmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline, TagTublerinline]

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,Productadmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(contant_us)