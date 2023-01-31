from django.db import models
from django import forms


class Information(models.Model):
    fooditem = models.CharField(max_length=50)
    marketcost = models.IntegerField()
    member = models.IntegerField()
    date = models.DateField(auto_now=True)


class Meal(models.Model):
    Shakil=models.IntegerField(default=0)
    Sadik=models.IntegerField(default=0)
    Babu=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)