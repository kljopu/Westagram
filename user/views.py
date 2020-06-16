# user/views.py

from django.shortcuts import render

from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

class UserRegistrationView(CreateView):     # 회원가입
    model =  get_user_model()
    form_class = UserRegistrationForm
    success_url = "/article/"

class UserLoginView(LoginView):             # 로그인 
    template_name = "user/login_form.html"

    def form_invalid(self, form):
        messages.error(self.request, "로그인에 실패하였습니다.", extra_tag = "danger")
        return super().form_invalid(form)