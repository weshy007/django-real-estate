from django.db import models

# Create your models here.
class Listings(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    num_ofbedroom = models.IntegerField(blank=True, null=True)
    num_bathroom = models.IntegerField()
    square_footage =models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    # images
    
    def __str__(self):
        return self.title