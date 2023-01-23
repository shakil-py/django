from django.db import models

# Create your models here.


# class marketcost(models.Model):
#     marketcost = models.IntegerField(5)


# class item(models.Model):
#     item = models.CharField(max_length=50, default="None")


# class datetime(models.Model):
#     date = models.DateField(auto_now=True)

class Information(models.Model):
    fooditem = models.CharField(max_length=50)
    marketcost = models.IntegerField()
    member = models.IntegerField()
    date = models.DateField(auto_now=True)
