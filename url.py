from django.urls import path
from . import views
urlpatterns = [

    path('',views.RegistraionForm),
    path('RegistrationForm', views.RegistraionForm),
    path('home',views.home),
    path('About Us', views.AboutUs),
    path('Appoint Doctor', views.AppointDoctor),
    path('Login', views.Login),

]
