from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)