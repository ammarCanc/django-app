"""
Forms for the core application
"""

from news.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUser(UserCreationForm):
    """ Override default behaviour so that more info is requested """
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1' ,'password2' )
