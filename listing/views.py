from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Listings
from realtors.models import Realtor
from .choices import state_choice, bed_choice, price_choice 

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
    queryset_list=Listings.objects.order_by('-list_date')
    if 'keywords' in request.GET: 
        keyword=request.GET['keywords']
        if keyword:
            queryset_list=queryset_list.filter(description__icontains=keyword)
    if 'city' in request.GET: 
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)

    if 'state' in request.GET: 
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)
    if 'bedrooms' in request.GET: 
        bedroom=request.GET['bedrooms']
        if bedroom:
            queryset_list=queryset_list.filter(bedrooms__lte=bedroom)
    if 'price' in request.GET: 
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)


    paginator=Paginator(queryset_list,2)
    page=request.GET.get('page')
    paged_listing=paginator.get_page(page)

    context={
        'beds':bed_choice,
        'prices':price_choice,
        'states':state_choice,
        'listing':queryset_list
    }
    return render(request,'listings/search.html',context)


