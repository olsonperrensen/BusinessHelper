from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class OView(TemplateView):
    template_name = 'ticket/index.html'