from django.db import models
from django import forms


class Information(models.Model):
    fooditem = models.CharField(max_length=50)
    marketcost = models.IntegerField()
    member = models.IntegerField()
    date = models.DateField(auto_now=True)


class meal(models.Model):
    person_1=models.IntegerField(default=0)
    person_2=models.IntegerField(default=0)
    person_3=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)