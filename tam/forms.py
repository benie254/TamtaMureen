from django import forms
from tam.models import Contact, Profile 


class PreorderForm(forms.Form):
    your_name = forms.CharField(max_length=60)
    order_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')