from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FirstUserSignUpForm


class FirstUserSignUpView(CreateView):
    form_class = FirstUserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/first_user_sign_up.html'
