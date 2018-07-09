
from django.contrib.auth import login, logout
from django.urls import reverse_lazy  # A lazily evaluated version of reverse().
from django.views.generic import CreateView
from django.urls import reverse

from . import forms

# Blog views created by Carla

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
