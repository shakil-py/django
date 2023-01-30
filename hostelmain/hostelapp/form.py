from django import forms


class RadioButtonForm(forms.Form):
    SHAKIL = [
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'),
        ('option_3', 'Option 3'),
    ]
    choice = forms.ChoiceField(choices=SHAKIL, widget=forms.RadioSelect)
    
