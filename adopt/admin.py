from django.contrib import admin
from .models import Adoptdogpics
from .models import Adoptcatpics
from .models import Adoptbirdpics
from .models import Adoptsmallpetpics

# Register your models here.
class Adoptdogs(admin.ModelAdmin):
    list_display = ['id','dogname','dogdesc','dogimg']
admin.site.register(Adoptdogpics, Adoptdogs)
class Adoptcats(admin.ModelAdmin):
    list_display = ['id','catname','catdesc','catimg']
admin.site.register(Adoptcatpics, Adoptcats)

class Adoptbirds(admin.ModelAdmin):
    list_display = ['id','birdname','birddesc','birdimg']
admin.site.register(Adoptbirdpics, Adoptbirds)
class Adoptsmallpets(admin.ModelAdmin):
    list_display = ['id','smallpetname','smallpetdesc','smallpetimg']
admin.site.register(Adoptsmallpetpics, Adoptsmallpets)