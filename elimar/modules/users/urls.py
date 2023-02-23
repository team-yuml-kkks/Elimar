from django.urls import path

from .views import FirstUserSignUpView, UsersList

urlpatterns = [
    path(
        "first-signup/",
        FirstUserSignUpView.as_view(),
        name="first-sign-up",
    ),
    path(
        "list/",
        UsersList.as_view(),
        name="users-list",
    ),
]
