from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listing_houses, name=('listings')),
    path('add-listing/', views.listing_create, name=('add-listing')),

    path('listings/<pk>/', views.listing_detail, name=('listing-detail')),
    path('listings/<pk>/edit/', views.listing_update, name=('listing-detail-edit')),
    path('listings/<pk>/delete/', views.listing_delete, name=('listing-delete')),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)