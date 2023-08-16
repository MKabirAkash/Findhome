from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listings
from realtors.models import Realtor
from listing.choices import state_choice, bed_choice, price_choice 

# Create your views here.

def index(request):
    listings=Listings.objects.order_by('-list_date').filter(is_active=True)[:3]
    context={
        'listing':listings,
        'beds':bed_choice,
        'prices':price_choice,
        'states':state_choice 
    }

    return render(request,'pages/index.html',context)

def about(request):
    realtors=Realtor.objects.order_by('name')[:3]
    mvp_realtor=Realtor.objects.filter(is_mvp=True)[:1]
    context={
        'realtor':realtors,
        'mvp_real':mvp_realtor
    }

    return render(request,'pages/about.html',context)




