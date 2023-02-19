from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import FirstUserSignUpForm


class FirstUserSignUpView(CreateView):
    form_class = FirstUserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/first_user_sign_up.html'

    def dispatch(self, request, *args, **kwargs):
        if get_user_model().objects.first():
            return redirect(reverse("home"))
        
        return super().dispatch(request, *args, **kwargs)
