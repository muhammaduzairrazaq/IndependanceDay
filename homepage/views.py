from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def display(request):
    template = loader.get_template('independence.html')
    return HttpResponse(template.render())