from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField()
    category = models.CharField(max_length=127, default="")
    desc = models.CharField(max_length=1023, default="")
    color = models.CharField(max_length=255, default="")
    col = models.IntegerField(default=0)
    file = models.FileField(null=True, blank=True, upload_to="files/newFiles")
