"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from momhacks import views as core_views

from . import views
from .views import *

app_name = 'momhacks'

urlpatterns = [ 
    url('profile/', TemplateView.as_view(template_name="profile.html")),
    url('resources/', TemplateView.as_view(template_name="resources.html")),  
    url('details/', TemplateView.as_view(template_name="details.html")), 
    url('listing/', TemplateView.as_view(template_name="listing.html")), 
    url(r'^$', core_views.home, name="home"), 

    url(r'^login/$', auth_views.login, name='login'), 
    url(r'^logout/$', auth_views.logout, name='logout'), 
    url(r'^oauth/$', include('social_django.urls', namespace='social')),

    ]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'http://momgodb.com/complete/facebook'


