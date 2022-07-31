from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField()
    category = models.CharField(max_length=127, default="")
    desc = models.CharField(max_length=1023, default="")
    file = models.FileField(null=True, blank=True, upload_to="files/newFiles")
