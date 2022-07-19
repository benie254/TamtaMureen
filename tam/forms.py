from django import forms 


class PreorderForm(forms.Form):
    name = forms.CharField(max_length=60)
    date = forms.DateField()