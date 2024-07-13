from django.contrib import admin
from django.urls import path,include
# images from admin panel
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('', include('register.urls')),  
    path('', include('adopt.urls')),
    path('', include('products.urls')),
    path('', include('cart.urls')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #global url for images in media folder
