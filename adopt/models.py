from django.db import models

# Create your models here.
class Adoptdogpics(models.Model):
    dogname = models.CharField(max_length=15)
    dogdesc = models.CharField(max_length=100)
    dogimg = models.ImageField(upload_to='dog_pics')

class Adoptcatpics(models.Model):
    catname = models.CharField(max_length=15)
    catdesc = models.CharField(max_length=100)
    catimg = models.ImageField(upload_to='cat_pics')

class Adoptbirdpics(models.Model):
    birdname = models.CharField(max_length=15)
    birddesc = models.CharField(max_length=100)
    birdimg = models.ImageField(upload_to='bird_pics')
class Adoptsmallpetpics(models.Model):
    smallpetname = models.CharField(max_length=15)
    smallpetdesc = models.CharField(max_length=100)
    smallpetimg = models.ImageField(upload_to='smallpet_pics')