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


# class MyModel(models.Model):
#     OPTIONS_1 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
#     OPTIONS_2 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
#     OPTIONS_3 = [("option1", "Option 1"), ("option2", "Option 2"), ("option3", "Option 3")]
#     name=models.CharField(max_length=50,default="name")
#     choice_1 = models.IntegerField(choices=OPTIONS_3)
#     choice_2 = models.IntegerField(choices=OPTIONS_3)
#     choice_3 = models.IntegerField(choices=OPTIONS_3)

class meal(models.Model):
    name=models.CharField(max_length=50,default=False)
    meal1, meal2, meal3 = "meal_1", "meal_2", "meal_3"
    person_1 = [(meal1, "meal_1"), (meal2, "meal_2"), (meal3, "meal_3")]
    # person_2 = ["meal_1", "meal_2", "meal_3"]
    # person_3 = ["meal_1", "meal_2", "meal_3"]
    
    parson_1 = models.IntegerField(choices=person_1)
    # parson_1=models.IntegerField(choices=person_2)
    # parson_1=models.IntegerField(choices=person_3)
