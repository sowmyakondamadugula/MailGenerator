from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.core.mail import send_mail

urlpatterns = [
    path('', views.home, name='index'),
    path('register/', views.register_user, name='register_user'),
    path('mainpage/', views.mainpage_view, name='mainpage'),
    path('translate/', views.translate_text, name='translate_text'),
    path('send-email/', views.send_email, name='send_email'),
]
