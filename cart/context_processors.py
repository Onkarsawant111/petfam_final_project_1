# A context processor in Django is a Python function that takes a request from user as an argument and returns a dictionary of items to be added to the context of all templates. This allows you to make certain data globally available across all templates without having to pass it explicitly in every view.

from .cart import Cart

def cart(request): # in settings.py of petfam register this function in templates
    return {'cart':Cart(request)}

# If you have a shopping cart, a context processor can automatically provide the current cart's contents to all your templates, allowing you to display cart details in the header or footer without passing it manually from every view.