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


# class HostelappMillamaount(models.Model):
#     name = models.CharField(max_length=50)
#     meall = models.IntegerField()
#     date = models.DateField()

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         managed = False
#         db_table = 'hostelapp_millamaount'
from django.db import models

class MyModel(models.Model):
    OPTIONS_1 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
    OPTIONS_2 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
    OPTIONS_3 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
    name=models.CharField(max_length=50,default="name")
    choice_1 = models.IntegerField(choices=OPTIONS_3)
    choice_2 = models.IntegerField(choices=OPTIONS_3)
    choice_3 = models.IntegerField(choices=OPTIONS_3)
    def __str__(self) -> str:
        return self.name
