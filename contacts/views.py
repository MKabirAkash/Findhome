from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts

# Create your views here.
def contact(request):
    if request.method=='POST':
        this_list=request.POST['listing']
        this_list_id=request.POST['listing_id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        contact_user=request.POST['user_id']
        contact=Contacts(listing=this_list, listing_id=this_list_id, name=name, email=email, phone=phone, message=message, user_id=contact_user)
        contact.save()
        messages.success(request,'you query is sent')
        return redirect('index')
    else:
        return redirect('about')