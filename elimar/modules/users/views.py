from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import FirstUserSignUpForm
from .models import User


class FirstUserSignUpView(CreateView):
    form_class = FirstUserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/first_user_sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        if get_user_model().objects.first():
            return redirect(reverse("home"))

        return super().dispatch(request, *args, **kwargs)


class UsersList(ListView):
    model = User
    paginate_by = 20
    template_name = "users/users_list.html"


class UserDetailsEdit(UpdateView):
    model = User
    fields = [
        "email",
        "password",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    ]
    template_name = "users/user_details_edit.html"
    success_url = reverse_lazy("users-list")
