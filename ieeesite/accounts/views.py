from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from . import forms
from django.views import generic
# Create your views here.
class SignUp(generic.CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('accounts:login')
    template_name='accounts/signup.html'
