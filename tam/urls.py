from django.urls import path,re_path as url,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin', admin.site.urls,name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/signup', auth_views.LoginView.as_view(template_name='django_registration/registration_form.html'),name='signup'),
    path('accounts/profile', auth_views.LoginView.as_view(template_name='registration/login.html'),name='signin'),
    path('accounts/signout', auth_views.LogoutView.as_view(template_name='registration/login.html'),name='signout'),
    # path('',views.home,name='home'),
]
