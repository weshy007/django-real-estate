from django.db import models


# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    num_ofbedroom = models.IntegerField(blank=True, null=True)
    num_bathroom = models.IntegerField(blank=True, null=True)
    square_footage =models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='media/')
    
    def __str__(self):
        return self.title