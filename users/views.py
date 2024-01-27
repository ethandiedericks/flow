from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .managers import CustomUserManager


class SignUpView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


def guest_login(request):
    user = get_user_model().objects.filter(email="guest@gmail.com").first()

    if user:
        login(request, user)
    else:
        user = CustomUserManager.create_user("guest@gmail.com", "Binary7j*")
        login(request, user)

    messages.success(request, "Guest user logged in successfully.")
    return redirect("budget")
