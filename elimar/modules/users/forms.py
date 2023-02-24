from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class FirstUserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Enter a valid email address")
    is_superuser = forms.BooleanField(required=True, widget=forms.HiddenInput(), initial=True)
    is_staff = forms.BooleanField(required=True, widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "password1",
            "password2",
            "is_superuser",
            "is_staff",
        ]


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        ]
