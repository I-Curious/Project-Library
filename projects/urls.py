from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('sp_project/<value>', views.sp_project , name='sp_project'),
]
