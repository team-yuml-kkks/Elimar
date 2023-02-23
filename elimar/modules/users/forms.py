from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext as _


class FirstUserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    is_superuser = forms.BooleanField(required=True, widget=forms.HiddenInput(), initial=True)
    is_staff = forms.BooleanField(required=True, widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_superuser",
            "is_staff",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Field("email"),
                    Field("password1"),
                    Field("password2"),
                    css_class="col",
                ),
                Div(
                    Field("first_name"),
                    Field("last_name"),
                    css_class="col",
                ),
                Field("is_superuser"),
                Field("is_staff"),
                Div(
                    Submit(
                        "submit",
                        _("Sign up"),
                        css_class="btn elimar-primary-btn mt-2",
                    ),
                    css_class="card-save",
                ),
                css_class="row",
            )
        )


class UserCreateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        ]
