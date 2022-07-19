from django.shortcuts import render
from django.contrib.auth.models import User
from tam.models import Menu, Profile 
import datetime as dt


# Create your views here.
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    details = Profile.objects.all().last()

    user = request.user
    username = user.username 
    message = 'Welcome, ' + username
    return render(request,'user/profile.html',{"profile":profile,"details":details,"message":message})

def home(request):
    date_today = dt.date.today()
    user = request.user
    username = user.username 
    message = 'Welcome, ' + username 

    menus = Menu.objects.all()
    return render(request,'content/index.html',{"message":message,"menus":menus,"date_today":date_today})

def menu(request,menu_id):
    menu = Menu.objects.all().filter(pk=menu_id)
    return render(request,'content/menu.html',{"menu":menu})