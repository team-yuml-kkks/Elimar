from django.urls import path

from .views import FirstUserSignUpView, UserCreate, UserDetailsEdit, UsersList

urlpatterns = [
    path(
        "first-signup/",
        FirstUserSignUpView.as_view(),
        name="first-sign-up",
    ),
    path(
        "",
        UsersList.as_view(),
        name="users-list",
    ),
    path(
        "<int:pk>/",
        UserDetailsEdit.as_view(),
        name="user-details-edit",
    ),
    path(
        "create/",
        UserCreate.as_view(),
        name="user-create",
    ),
]
