from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from tam_app.serializers import QuoteSerializer
from tam_app.models import Contact, Menu, Profile,Preorder, Quote
import datetime as dt
from datetime import datetime 
import time 
from tam_app.forms import ContactForm, PreorderForm, ProfileForm
from django.db.models import Max 
import random 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from tam_app.requests import get_quotes


# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profile = User.objects.all().filter(pk=user_id)
    details = Profile.objects.all().filter(pk=user_id)
    updated_details = Profile.objects.all().last()
    quotes = get_quotes()

    if request.method == 'POST':
        proform = ProfileForm(request.POST)
        if proform.is_valid():
            print('profile valid!')
            bio = proform.cleaned_data['bio']
            # profile_photo = proform.cleaned_data['profile_photo']
            profile_info = Profile(bio=bio,)
            profile_info.save()
            print(profile_info)
            return redirect('profile',user_id)
    else:
        proform = ProfileForm()

    user = request.user
    username = user.username 
    message = 'Welcome, ' + username
    return render(request,'user/profile.html',{"profile":profile,"details":details,"message":message,"updated_details":updated_details,"proform":proform,"username":username,"quotes":quotes})

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
    ingredients = Menu.objects.all()

    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            print('contact valid!')
            name = contactform.cleaned_data['name']
            email = contactform.cleaned_data['email']
            message = contactform.cleaned_data['message']
            contact = Contact(name=name,email=email,message=message)
            contact.save()
            receiver = 'beniewrites@gmail.com'
            
            print(message)
            contact_email(name,email,message,receiver)
            emailmsg = contact_email(name,email,message,receiver)
            print(emailmsg)
            
            return redirect('contact-success')
    else:
        contactform = ContactForm()
    return render(request,'content/landing.html',{"super":super,"ingredients":ingredients,"contactform":contactform})

def contact(request):
    contact = Contact.objects.all().last()
    return render(request,'content/contact_success.html',{"contact":contact})

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
            menu_item = preform.cleaned_data['menu_item']
            item_cost = preform.cleaned_data['item_cost']
            your_name = preform.cleaned_data['your_name']
            your_email = preform.cleaned_data['your_email']
            your_mobile = preform.cleaned_data['your_mobile']
            order_date = preform.cleaned_data['order_date']
            order_info = Preorder(order_date=order_date,your_name=your_name,your_email=your_email,your_mobile=your_mobile,menu_item=menu_item,item_cost=item_cost)
            order_info.save()
            email = 'beniewrites@gmail.com'
            
            print(order_info)
            orderinfo_email(menu_item,item_cost,your_name,your_email,your_mobile,order_date,email)
            emailmsg = orderinfo_email(menu_item,item_cost,your_name,your_email,your_mobile,order_date,email)
            print(emailmsg)
            
            return redirect('checkout',menu_id)
    else:
        preform = PreorderForm()
    
    return render(request,'content/menu.html',{"menu":menu,"preform":preform})

def checkout(request,menu_id):
    menu = Menu.objects.all().filter(pk=menu_id)
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
        message = "You haven't searched anything yet!"
        return render(request,'content/search_results.html',{"message":message})

class RandomMealQuotes(APIView):
    def get(self,request,format=None):
        quotes = Quote.objects.all().aggregate(quotes=Max("id"))['quotes']
        pk = random.randint(1,quotes)
        random_quote = Quote.objects.get(pk=pk)
        serializers = QuoteSerializer(random_quote,many=False)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = QuoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
