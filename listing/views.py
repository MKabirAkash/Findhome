from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Listings
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings=Listings.objects.order_by('-price').filter(is_active=True)
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listing=paginator.get_page(page)
    context={
        'listing':paged_listing
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    list=get_object_or_404(Listings,pk=listing_id)
    real=Realtor.objects.filter(name=list.realtor)
    context={
        'list':list,
        'real':real
    }
    return render(request,'listings/listing.html',context)

def search(request):
    #return HttpResponse('<h1>This is my about page</h1>')
    return render(request,'listings/search.html')


