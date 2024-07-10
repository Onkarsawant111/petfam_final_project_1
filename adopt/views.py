from django.shortcuts import render
from .models import Adoptdogpics
from .models import Adoptcatpics
from .models import Adoptbirdpics   
from .models import Adoptsmallpetpics

# Create your views here.
def dog(request):
    dog_pics = Adoptdogpics.objects.all()
    return render(request, 'adopt_dog.html', {'dogs':dog_pics})

def cat(request):
    cat_pics = Adoptcatpics.objects.all()
    return render(request, 'adopt_cat.html', {'cats':cat_pics})

def bird(request):
    bird_pics = Adoptbirdpics.objects.all()
    return render(request, 'adopt_bird.html', {'birds':bird_pics})

def smallpet(request):
    smallpet_pics = Adoptsmallpetpics.objects.all()
    return render(request, 'adopt_smallpet.html',{'smallpets': smallpet_pics})