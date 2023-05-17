from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from .forms import UserSignUpForm


class SignUp(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')  # Przekierowanie po udanej rejestracji
    template_name = 'accounts/signup.html'

class SignUpView(FormView):

    def form_valid(self, form):
        form.save()  # Zapisanie nowego użytkownika
        return super().form_valid(form)