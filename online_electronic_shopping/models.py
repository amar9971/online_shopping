from django.db import models

# Create your models here.

class Categories(models.Model):
    name= models.CharField(max_length=200)


class Brand(models.Model):
    name= models.CharField(max_length=200)


class Color(models.Model):
    name= models.CharField(max_length=200)
    code= models.CharField(max_length=50)

class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('1000 TO 10000','1000 TO 10000'),
        ('10000 TO 20000','10000 TO 20000'),
        ('40000 TO 50000','40000 TO 50000'),
        ('60000 TO 80000','60000 TO 80000'),
        ('100000 TO 200000','100000 TO 200000'),
    )
    price= models.CharField(choices=FILTER_PRICE, max_length=60)

