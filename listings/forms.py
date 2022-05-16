from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'price',
            'num_ofbedroom',
            'num_bathroom',
            'square_footage',
            'address',
            'image'
        ]