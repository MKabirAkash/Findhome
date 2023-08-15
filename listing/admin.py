from django.contrib import admin
from .models import Listings

class Listingadmin(admin.ModelAdmin):
    list_display=('title','address','realtor','price','is_active','list_date')
    list_display_links=('title','address')
    list_filter=('realtor','title',)
    #list_editable=('is_active',)
    search_fields=('title','address','city','state','price')

admin.site.register(Listings,Listingadmin)
