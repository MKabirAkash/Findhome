from django.contrib import admin
from .models import Realtor

class Realtoradmin(admin.ModelAdmin):
    list_display=('name','email','hire_date')
    list_display_links=('name',)
    search_fields=('name','description')

admin.site.register(Realtor,Realtoradmin)
