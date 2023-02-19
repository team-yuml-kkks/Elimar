from django.urls import path

from .views import FirstUserSignUpView

urlpatterns = [
    path(
        "first-signup/",
        FirstUserSignUpView.as_view(),
        name="first-sign-up",
    ),
]
