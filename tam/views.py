from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from tam.email import orderinfo_email
from tam.models import Menu, Profile,Preorder, Super
import datetime as dt
from datetime import datetime 
import time 
from tam.forms import PreorderForm, ProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    details = Profile.objects.all().filter(pk=user_id)
    updated_details = Profile.objects.all().last()

    if request.method == 'POST':
        proform = ProfileForm(request.POST)
        if proform.is_valid():
            print('profile valid!')
            bio = proform.cleaned_data['bio']
            profile_info = Profile(bio=bio,)
            profile_info.save()
            print(profile_info)
            return redirect('profile',user_id)
    else:
        proform = ProfileForm()

    user = request.user
    username = user.username 
    message = 'Welcome, ' + username
    return render(request,'user/profile.html',{"profile":profile,"details":details,"message":message,"updated_details":updated_details,"proform":proform})

@login_required(login_url='/accounts/login/')
def updatebio(request):
    user = request.user
    if request.method == 'POST':
        proform = ProfileForm(request.POST)
        if proform.is_valid():
            print('profile valid!')
            bio = proform.cleaned_data['bio']
            profile_info = Profile(bio=bio,)
            profile_info.save()
            print(profile_info)
            return redirect('profile',user.id)
    else:
        proform = ProfileForm()
    
    return render(request,'user/update-bio.html',{'proform':proform})

def landing(request):
    super = Super.objects.all().last()
    return render(request,'content/landing.html',{"super":super})

def home(request):
    date_today = dt.date.today()
    # date_today = datetime.now()  # prints both date & time using settings local time
    user = request.user
    username = user.username 
    message = 'Welcome, ' + username 

    menus = Menu.objects.all()
    return render(request,'content/index.html',{"message":message,"menus":menus,"date_today":date_today})

@login_required(login_url='/accounts/login/')
def menu(request,menu_id):
    menu = Menu.objects.all().filter(pk=menu_id)
    # preform = PreorderForm()

    if request.method == 'POST':
        preform = PreorderForm(request.POST)
        if preform.is_valid():
            print('preorder valid!')
            name = preform.cleaned_data['name']
            date = preform.cleaned_data['date']
            order_info = Preorder(date=date,name=name)
            order_info.save()
            email = 'beniewrites@gmail.com'
            
            print(order_info)
            orderinfo_email(name,date,email)
            emailmsg = orderinfo_email(name,date,email)
            print(emailmsg)
            
            return redirect('checkout')
    else:
        preform = PreorderForm()
    
    return render(request,'content/menu.html',{"menu":menu,"preform":preform})

def checkout(request):
    preorder = Preorder.objects.all().last()
    return render(request,'content/checkout.html',{"menu":menu,"preorder":preorder})

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
