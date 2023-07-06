from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
    path("",views.loginUser, name="login"),
    path("register",views.register,name="register"),
    path("home",views.homePage,name="home")
]
