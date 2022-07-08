from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="prod")
    price = models.IntegerField()
    desc = models.CharField(max_length=1023, default="")
    file = models.FileField(null=True, blank=True, upload_to="files/newFiles")
