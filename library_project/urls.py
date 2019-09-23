from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views

#The main file of all the urls, this is the first file which is scanned when link is entered
urlpatterns = [
    path('admin/', admin.site.urls), #For admin site
    path('',include('index.urls')), #for index or main page will be redirected to the urls present in index folder
    path('about/',include('about.urls')), #for about page
    path('mentor/',include('mentor.urls')), #for folder urls
    path('mailus/',include('mailus.urls')), #mailus folder urls
    path('projects/',include('projects.urls')), #project folder urls

    #Handling user data and links 
    path('register/', user_views.register, name='register'), #for registeration
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
    #Complusary needed for reseting the password
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
]
