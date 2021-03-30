from django.contrib import admin
from django.urls import path

from . import views,facebook,wallet,task,login

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.creae),
    path('Login',views.login),
    path('logout',views.logout),
    path('facebook',facebook.facebook),
    path("facebookVerification",facebook.verification),
    path('wallet',wallet.index),
    path ('task',task.index),
    path("complet",task.complet),
    path("Login",login.index)
    ]