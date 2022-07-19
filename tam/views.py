from django.shortcuts import render
from django.contrib.auth.models import User
from tam.models import Profile 


# Create your views here.
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    details = Profile.objects.all().last()
    user = request.user
    username = user.username 
    message = 'Welcome, ' + username
    print(details)
    return render(request,'user/profile.html',{"profile":profile,"details":details,"message":message})

def home(request):
    user = request.user
    username = user.username 
    profile = User.objects.all().filter(pk=user.id)
    message = 'Welcome, ' + username 
    return render(request,'content/index.html',{"profile":profile,"message":message})