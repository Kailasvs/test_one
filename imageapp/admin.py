from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from . models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display=('name','image')
    
    

admin.site.register(Photo,PhotoAdmin)