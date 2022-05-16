from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm

# Create your views here.
# CRUD - Create, Retrive, Update, Delete, & List functionality

# LISTS ALL THE ADDED HOUSES IN THE DB
def listing_houses(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, 'listings.html', context)

# SHOWING THE DETAILS OF A SPECIFIC HOUSE WITH THE PRIMARY KEY
def listing_detail(request, pk):
    listing = Listing.objects.get(pk=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing_details.html", context)

# LISTING CREATE WITH DJANGO MODEL FORMS
def listing_create(request):
    form = ListingForm()

    if request.method == " POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    # If the form is not valid, they are directed to submit another form
    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)

# UPDATING DETAILS FROM A SPECIFIC HOUSE
def listing_update(request, pk):
    listing = Listing.objects.get(pk=pk)
    form = ListingForm(instance=listing)

    if request.method == " POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    # If the form is not valid, they are directed to submit another form
    context = {
        'form': form
    }
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(pk=pk)
    listing.delete()
    return redirect("/")
