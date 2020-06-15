from django.shortcuts import render

from django.views.generic import CreateView

from user.models import User

class UserRegistrationView(CreateView):
    model =  User
    fields = (
        'email', 'name', 'password'
    )
