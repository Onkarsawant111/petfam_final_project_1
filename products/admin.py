from django.contrib import admin
from .models import Categories
from .models import Customers
from .models import Products
from .models import Orders
# Register your models here.
class Admin_categories(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Categories, Admin_categories)

class Admin_customers(admin.ModelAdmin):
    list_display = ['name','phone','email','password']
admin.site.register(Customers, Admin_customers)

class Admin_products(admin.ModelAdmin):
    list_display = ['name', 'price','category','image']
admin.site.register(Products, Admin_products)

class Admin_orders(admin.ModelAdmin):
    list_display = ['product','customer','quantity','address','phone','date','status']
admin.site.register(Orders, Admin_orders)