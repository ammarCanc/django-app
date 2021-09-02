"""
Views for the Core application
"""
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = CreateUser
    success_message = "Your profile was created successfully"
