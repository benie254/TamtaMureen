from django import forms
from tam.models import Contact, Menu, Preorder, Profile 


class PreorderForm(forms.ModelForm):
    class Meta:
        model = Preorder
        fields = ('menu_item','item_cost','your_name','your_email','your_mobile','order_date')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')