from django.test import TestCase
from tam.models import Profile,ingredient,Menu 

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.janja = Profile(bio='Aloha',address='Nairobi',profile_photo='https://cloudinary.benie.png',mobile_number='0712345678',status='active')

    def test_instance(self):
        self.assertTrue(isinstance(self.janja,Profile))

    def test_save_method(self):
        self.janja.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class ingredientTestClass(TestCase):
    def setUp(self):
        self.pepper = ingredient(name='pepper')

    def test_instance(self):
        self.assertTrue(isinstance(self.pepper,ingredient))

    def test_save_method(self):
        self.pepper.save_ingredient()
        ingredients = ingredient.objects.all()
        self.assertTrue(len(ingredients)>0)


class MenuTestClass(TestCase):
    def setUp(self):
        self.royco = ingredient(name='royco')
        self.royco.save()

        self.new_menu = Menu(name='Mandazi Special',description='A rare African delicacy',snap='https://cloudinary.benie2.png',status='available')
        self.new_menu.save()

        self.new_menu.ingredients.add(self.royco)

    
    def tearDown(self):
        ingredient.objects.all().delete()
        Menu.objects.all().delete()

    
    def test_search_by_ingredient(self):
        search_by_ingredient = Menu.objects.filter(ingredients__name=self)
        return search_by_ingredient

    
    def test_get_by_id(self):
        get_by_id = Menu.objects.filter(id=self.id)
        return get_by_id

    
    def test_update_menu(self):
        self.updated_ingredient = ingredient(name='white pepper')
        self.updated_ingredient.save()

        self.updated_menu = Menu.objects.filter(name=self).update(name='Chapati',description='The only thing you will eat',snap='https://cloudinary.benie3.png',status='awaiting request')
