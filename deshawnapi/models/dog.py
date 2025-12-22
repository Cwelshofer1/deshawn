from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
