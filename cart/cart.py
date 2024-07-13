# When a user interacts with your web application, the server creates a session, which is a temporary storage space to hold user-specific data (like a shopping cart). This data resides on the server. The server generates a unique session identifier (session ID) for each session. This ID is usually sent to the client's web browser as a cookie. The browser stores this cookie, which helps the server recognize subsequent requests from the same user.When the user makes further requests (e.g., navigating to different pages), the browser sends the session ID back to the server via the cookie. This allows the server to retrieve the corresponding session data and continue maintaining the user's state (like their shopping cart).
from products.models import Products
class Cart():
    def __init__(self, request):
        # below code allows the Cart class to interact with the user's session data, enabling operations like storing, retrieving, or modifying items in the shopping cart. This facilitates maintaining user state across multiple requests.
        self.session = request.session
        # get the current session key from server if it exists :
        cart = self.session.get('session_key')
        # if the user is new then create session key and it initializes an empty cart as a dictionary and stores it in the session under the key 'cart'. This allows you to maintain an empty shopping cart for new users.
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # below code makes sure cart is available on all pages of project
        self.cart = cart

    def add(self, product): # this function is called by --> cart.add(product = product) in views.py of 'cart' app
        product_id = str(product.id)
        # if product is already present in the class then :
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        # modify the session
        self.session.modified = True

    def __len__(self): # It filters to get the length of cart i.e total no of product present in cart and siplay it on cart logo navbar
        return len(self.cart)
    
    def get_prods(self): # it shows what is it inside cart that we got from above add()
        product_ids = self.cart.keys() #get id from cart
        products = Products.objects.filter(id__in=product_ids)  # use id to look for products in Product models
        return products










