from django.shortcuts import render
from .models import Listing

# Create your views here.
# CRUD - Create, Retrive, Update, Delete, & List functionality

# LISTS ALL THE ADDED HOUSES IN THE DB
def listing_houses(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, 'listings.html', context)

# SHOWING THE DETAILS OF A SPECIFIC HOUSE
def listing_detail(request, pk):
    listing = Listing.objects.get(pk=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing_details.html", context)

def listing_list(request):
    pass

def listing_update(request):
    pass

def listing_delete(request):
    pass