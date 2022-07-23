from django import forms
from tam.models import Contact, Profile 


class PreorderForm(forms.Form):
    name = forms.CharField(max_length=60)
    date = forms.DateField(
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