from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'),name='logout'),
    path('',views.home,name='home'),
]