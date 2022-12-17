from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import ReviewForm
from .models import Review
from django.http import HttpResponse
# Create your views here.

class OView(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'ticket/index.html'
    success_url = 'ty'

def ty(req):
    return HttpResponse('ty')