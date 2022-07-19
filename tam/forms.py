from django import forms 


class PreorderForm(forms.Form):
    date = forms.DateInput(label='Your Requested Date')