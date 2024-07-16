from django.contrib import admin
from .models import Categories, Orders, Products, Customers
from .models import Customer_profile
from django.contrib.auth.models import User

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

#mix customer_profile and User model together 
class Profileinline(admin.StackedInline):
    model = Customer_profile
# extend/ update User model i.e what can be shown on admin panel 
class Useradmin(admin.ModelAdmin):
    model = User  # we want to update User model & inside that we want to display:
    field = ['username','password','firstname','email']
    inlines = [Profileinline] # to show everything else other than User model fields we use this 

#but before this new registration of fields in our User model's admin panel we need to unregister the old registration and carry out new registration
admin.site.unregister(User)
# new registration 
admin.site.register(User, Useradmin)
