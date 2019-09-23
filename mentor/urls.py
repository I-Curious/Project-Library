from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mentor-home'),
    path('sp_mentor/<value>',views.sp_mentor, name='sp_mentor'),
]
