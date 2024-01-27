from django.urls import path

from .views import SignUpView, guest_login

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("guest-login/", guest_login, name="guest_login"),
]
