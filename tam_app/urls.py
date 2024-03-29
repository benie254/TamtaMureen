from django.urls import path,re_path as url,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/signin', auth_views.LoginView.as_view(template_name='registration/login.html'),name='signin'),
    path('accounts/signout', auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='signout'),
    path('accounts/profile/',auth_views.LoginView.as_view(template_name='registration/login_success.html'),name='signin-success'),
    path('user/profile/<user_id>/',views.profile,name='profile'),

    path('',views.landing,name='landing'),
    path('home',views.home,name='home'),
    path('menu/<menu_id>',views.menu,name='menu'),
    path('menus/search-by-ingredient-results',views.search_by_ingredient,name='search-results'),
    path('menu/pre-order/checkout/<menu_id>',views.checkout,name='checkout'),
    path('user/update-bio',views.updatebio,name='update-bio'),
    path('user/contact-success',views.contact,name='contact-success'),

    path('api/meal-quotes/random',views.RandomMealQuotes.as_view(),name='random-quotes')

    # url(r'^ajax/preorder/$',views.sendpreorder,name='send-preorder'),
]
