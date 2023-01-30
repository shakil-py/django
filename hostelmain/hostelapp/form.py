from django import forms


class RadioButtonForm(forms.Form):
    OPTIONS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    shakil = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)
    sadik = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)
    babu = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)
