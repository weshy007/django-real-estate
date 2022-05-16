from . import views
from django.urls import path

urlpatterns = [
    path('', views.listing_houses, name=('listings')),
    path('listings/<pk>', views.listing_detail, name=('listing-detail')),
]