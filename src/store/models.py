from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    description = models.CharField(max_length=1024)
    image_path = models.CharField(max_length=256)
    stock = models.IntegerField()
    created_at = models.DateTimeField( default= timezone.now )