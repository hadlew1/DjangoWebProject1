"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include, url
import ERPApp.views



urlpatterns = [
    url(r'^$', ERPApp.views.index, name='index'),
    url(r'^home$', ERPApp.views.index, name='home'),
    url(r'^about$', ERPApp.views.about, name ='about'),
]
