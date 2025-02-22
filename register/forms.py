from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from products.models import Customer_profile

# django-form is used to create new user in our User model in admin panel 
class Register(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('first_name','username','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Name'
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password' 

# adding additional info in admin panel
class Userinfo(forms.ModelForm): 
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Customer_profile
        fields= ('phone', 'address')