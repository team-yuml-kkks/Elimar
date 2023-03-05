from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import FirstUserSignUpForm, UserCreateForm, LoginUserForm
from .models import User


class FirstUserSignUpView(CreateView):
    form_class = FirstUserSignUpForm
    success_url = reverse_lazy("users-login")
    template_name = "registration/first_user_sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        if get_user_model().objects.first():
            return redirect(reverse("home"))

        return super().dispatch(request, *args, **kwargs)


class UsersList(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 20
    template_name = "users/users_list.html"


class UserCreate(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy("users-list")


class UserDetailsEdit(LoginRequiredMixin, UpdateView):
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


class LoginUserView(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy("users-login")
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(LoginUserView, self).form_valid(form)
