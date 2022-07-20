from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from tam.email import orderinfo_email
from tam.models import Menu, Profile,Preorder
import datetime as dt
from datetime import datetime 
import time 
from tam.forms import PreorderForm


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
    # date_today = datetime.now()  # prints both date & time using settings local time
    user = request.user
    username = user.username 
    message = 'Welcome, ' + username 

    menus = Menu.objects.all()
    return render(request,'content/index.html',{"message":message,"menus":menus,"date_today":date_today})

def menu(request,menu_id):
    menu = Menu.objects.all().filter(pk=menu_id)
    # preform = PreorderForm()

    if request.method == 'POST':
        preform = PreorderForm(request.POST)
        if preform.is_valid():
            name = preform.cleaned_data['name']
            date = preform.cleaned_data['date']
            order_info = Preorder(date=date,name=name)
            order_info.save()
            email = 'beniewrites@gmail.com'
            
            print(order_info)
            orderinfo_email(name,date,email)
            emailmsg = orderinfo_email(name,date,email)
            print(emailmsg)
            
            HttpResponseRedirect('home')
            print('preorder valid!')
    else:
        preform = PreorderForm()
    
    return render(request,'content/menu.html',{"menu":menu,"preform":preform})

def sendpreorder(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    email = request.POST.get('email')
    orderinfo = Preorder(name=name,date=date,email=email)
    orderinfo.save()
    orderinfo_email(name,email)
    data = {'success':'A preorder has been placed!'}
    return JsonResponse(data)

def search_by_ingredient(request):
    if 'menu' in request.GET and request.GET["menu"]:
        ingredient_term = request.GET.get("menu")
        searched_menus = Menu.search_by_ingredient(ingredient_term)
        message = f"{ingredient_term}"
        return render(request,'content/search_results.html',{"message":message,"searched_menus":searched_menus})
    else:
        message = "You haven't searched anything yet."
        return render(request,'content/search_results.html',{"message":message})

def preorder(request,menu_id):
    menu = Menu.objects.all().filter(pk=menu_id)
    user = request.user 

    
    return render(request,'content/pre-order.html',{"meu":menu,"user":user})