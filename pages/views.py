from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listings
from realtors.models import Realtor 

# Create your views here.

def index(request):
    listings=Listings.objects.order_by('-list_date').filter(is_active=True)[:3]
    context={
        'listing':listings
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

def featured(request):
    #return HttpResponse('<h1>This is my about page</h1>')
    return render(request,'pages/featured.html')


