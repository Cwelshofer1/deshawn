from django.db import models
from .city import City

class Walker(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
