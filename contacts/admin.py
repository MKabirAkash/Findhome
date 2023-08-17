from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display=('name','listing','email','phone','contact_date')
    list_display_links=('name',)

admin.site.register(Contacts,ContactsAdmin)