from django.shortcuts import render
from django.contrib.auth.models import User 


# Create your views here.
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    return render('profile.html',{"profile":profile})