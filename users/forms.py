from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#USed for creating custom forms rather than using the default forms provided by django
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
