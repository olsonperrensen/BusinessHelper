from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, TemplateView, DetailView
from .models import Ticket
from sec.models import User
from django.http import HttpResponse
# Create your views here.


class CreateView(CreateView):
    template_name = 'ticket/create.html'
    model = Ticket
    fields = '__all__'
    success_url = 'ty'


class ty(TemplateView):
    template_name = 'ticket/ty.html'


class ListView(ListView):
    template_name = 'ticket/list.html'
    model = Ticket


class DetailView(DetailView):
    template_name = 'ticket/one.html'
    model = Ticket

class UpdateView(UpdateView):
    template_name = 'ticket/update.html'
    model = Ticket
    fields = '__all__'
    success_url = 'list'

class DeleteView(DeleteView):
    template_name = 'ticket/delete.html'
    model = Ticket
    fields = '__all__'
    success_url = 'list'


class TemplateView(TemplateView):
    template_name = 'ticket/team.html'
