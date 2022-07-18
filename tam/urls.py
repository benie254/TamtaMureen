from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin', admin.site.urls,name='admin'),
    path('accounts/signin', auth_views.LoginView.as_view(template_name='registration/login.html'),name='signin'),
    path('accounts/signout', auth_views.LogoutView.as_view(template_name='registration/login.html'),name='signout'),
    # path('',views.home,name='home'),
]
