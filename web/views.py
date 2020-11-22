from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

class LogIn(TemplateView):
    template_name = 'login.html'

class Registar(TemplateView):
    template_name = 'register.html'

