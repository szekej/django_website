from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
