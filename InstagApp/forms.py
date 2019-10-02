from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from InstagApp.models import InstagUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstagUser
        fields = ('username', 'email', 'profile_img')
