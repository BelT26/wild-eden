from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Plant(models.Model):
    """
    A model for plants listed for sale
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    season = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.name)
