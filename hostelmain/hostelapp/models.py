from django.db import models



class Information(models.Model):
    fooditem = models.CharField(max_length=50)
    marketcost = models.IntegerField()
    member = models.IntegerField()
    date = models.DateField(auto_now=True)

from django import forms

class RadioButtonForm(forms.Form):
    CHOICES = [
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'),
        ('option_3', 'Option 3'),
    ]
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
