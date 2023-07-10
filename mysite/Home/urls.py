from django.urls import path

from . import views

urlpatterns = [
    path("", views.signupCompany, name="signupCompany"),
    path("login/", views.loginCompany, name="loginCompany"),
    path("home/", views.home, name="home"),
    path("accessories/<str:id>", views.accessories, name="accessories"),
    path("logout/", views.logoutCompany, name="logoutCompany"),
    path("home/<str:id>", views.employ, name="employ"),

]