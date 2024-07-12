from django.db import models
import datetime

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customers(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name  
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products_pics')

    def __str__(self):
        return self.name
class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15,default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product.name} - {self.customer.name} - {self.date}"
