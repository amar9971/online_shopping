from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Categories(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Color(models.Model):
    name= models.CharField(max_length=200)
    code= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('1000 TO 10000','1000 TO 10000'),
        ('10000 TO 20000','10000 TO 20000'),
        ('40000 TO 50000','40000 TO 50000'),
        ('60000 TO 80000','60000 TO 80000'),
        ('100000 TO 200000','100000 TO 200000'),
    )
    price= models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price


class Product(models.Model):
    CONDITION= (('New', 'New'),('Old','Old'))
    STOCK = (('In Stock','In Stock'), ('Out Of Stock','Out Of Stock'))
    STATUS= (('Publish','Publish'),('Draft','Draft'))

    unique_id = models.CharField(unique=True, max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to='Product_image/img')
    name= models.CharField(max_length=200)
    price= models.IntegerField()
    condition= models.CharField(choices=CONDITION,max_length=100)
    information= RichTextField(null=True)
    discription = RichTextField(null=True)
    stock= models.CharField(choices=STOCK, max_length=200)
    status= models.CharField(choices=STATUS, max_length=100)
    created_date= models.DateTimeField(default=timezone.now)

    Categories= models.ForeignKey(Categories, on_delete=models.CASCADE)
    Brand= models.ForeignKey(Brand,on_delete=models.CASCADE)
    Color = models.ForeignKey(Color, on_delete=models.CASCADE)
    Filter_Price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id= self.created_date.strftime('75%Y%m%d23') + str(self.id)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Images(models.Model):
    image= models.ImageField(upload_to='Product_image/img')
    product= models.ForeignKey(Product,on_delete=models.CASCADE)




class Tag(models.Model):
    name= models.CharField(max_length=200)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)

class contant_us(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    subject= models.CharField(max_length=300)
    massege= models.TextField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

#class login