from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    img =  models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=64)
    price = models.IntegerField()