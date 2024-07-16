from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # it helps to create automatically user_profile model when user register on our website

# Create your models here.
# It is created to add extra fileds like phone no, address in User model 
class Customer_profile(models.Model): # creating model and display this model on admin panel once we register new user in User model.
    user = models.OneToOneField(User, on_delete= models.CASCADE) # it has one to one relation i.e. only one profile created for one user
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
# create user/customer   profile by default once it registers
def create_customer_profile(sender, instance, created, **kwargs): #instance means current logged in info 
    if created: # if user is registered
        user_profile = Customer_profile(user = instance)
        user_profile.save()

post_save.connect(create_customer_profile, sender=User)  # it connects both 'User' and 'Customer_profile' models automatically 

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
