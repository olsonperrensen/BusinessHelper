from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Ticket
from django.http import HttpResponse
# Create your views here.


class CreateView(CreateView):
    template_name = 'ticket/create.html'
    model = Ticket
    fields = '__all__'
    success_url = 'ty'

def ty(req):
    return HttpResponse('ty')

class ListView(ListView):
    template_name = 'ticket/list.html'
    model=Ticket