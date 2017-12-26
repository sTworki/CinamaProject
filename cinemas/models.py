from django.db import models


# Create your models here.

class Chain(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    chain = models.ForeignKey(Chain, on_delete=models.DO_NOTHING)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    address_line3 = models.CharField(max_length=50)
    post_code = models.CharField(max_length=20)

