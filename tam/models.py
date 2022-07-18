from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=250)
    address = models.CharField(max_length=60)
    profile_photo = CloudinaryField('Profile photo')
    mobile_no = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    CHOICES = (('ac','active'),('aw','away'))
    status = models.CharField(max_length=60,choices=CHOICES)

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
    snap = CloudinaryField('Menu photo')
    CHOICES = (('ck','cooking',),('ar','awaiting request'),('av','available'))
    status = models.CharField(max_length=60,choices=CHOICES)
    ingredients = models.ManyToManyField(ingredient)
    cook = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    @classmethod
    def menus(cls):
        menus = cls.objects.all()
        return menus

    @classmethod
    def search_by_ingredient(cls, ingredient_term):
        menu = cls.objects.filter(ingredients__name=ingredient_term)
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