from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'), #This is the path for the view of the about page
]
