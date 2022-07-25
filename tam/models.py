from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=60,null=True)
    about_me = models.CharField(max_length=500,null=True)
    profile_photo = CloudinaryField('Profile photo',null=True)
    address = models.CharField(max_length=150,null=True)
    email = models.EmailField(null=True)
    mobile_no = models.IntegerField(null=True)
    CHOICES = (('active','active'),('away','away'))
    status = models.CharField(max_length=60,choices=CHOICES,null=True)

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=250,null=True)
    profile_photo = CloudinaryField('image', null=True)
    CHOICES = (('active','active'),('away','away'))
    status = models.CharField(max_length=60,choices=CHOICES,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        updated_profile = self.update(bio=self.bio,address=self.address,profile_photo=self.profile_photo,mobile_no=self.mobile_no,status=self.status)
        return updated_profile


class ingredient(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_ingredient(self):
        self.save()

    def delete_ingredient(self):
        self.delete()

    def update_ingredient(self):
        updated_ingredient = self.update(name=self.name)
        return updated_ingredient


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cost = models.DecimalField(decimal_places=2,max_digits=3)
    snap = CloudinaryField('Menu photo')
    CHOICES = (('cooking','cooking',),('awaiting request','awaiting request'),('available','available'))
    status = models.CharField(max_length=60,choices=CHOICES)
    ingredients = models.ManyToManyField(ingredient)
    cook = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.description

    @classmethod
    def menus(cls):
        menus = cls.objects.all()
        return menus

    @classmethod
    def search_by_ingredient(cls, ingredient_term):
        menu = cls.objects.filter(ingredients__name__icontains=ingredient_term)
        return menu 

    @classmethod 
    def get_by_id(cls,id):
        menu = cls.objects.filter(id=id)
        return menu

    def save_menu(self):
        self.save()

    def delete_menu(self):
        self.delete()

    def update_menu(self):
        updated_menu = self.update(name=self.name,description=self.description,snap=self.snap,status=self.status)
        return updated_menu


class Preorder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    menu_item = models.CharField(max_length=60,null=True)
    item_cost = models.IntegerField(null=True)
    your_name = models.CharField(max_length=60,default='')
    your_mobile = models.IntegerField(null=True)
    your_email = models.EmailField(null=True)
    order_date = models.DateField(default=timezone.now)

class Contact(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=60,default='')
    message = models.TextField(max_length=60,default='')


class Quote(models.Model):
    quote = models.CharField(max_length=2000,default='')
    author = models.CharField(max_length=60,default='')
    source = models.URLField(max_length=500,default='')