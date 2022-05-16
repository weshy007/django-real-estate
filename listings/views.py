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

def listing_(request):
    pass

def listing_list(request):
    pass

def listing_update(request):
    pass

def listing_delete(request):
    pass