from django.shortcuts import render
from django.contrib.auth.models import User 


# Create your views here.
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    user = request.user
    message = 'Welcome, ' + user
    return render('user/profile.html',{"profile":profile,"message":message})

def home(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    user = request.user
    message = 'Welcome, ' + user
    return render('content/index.html',{"profile":profile,"message":message})