from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.

def display(request):
    a = 'NO!'
    time = dt.datetime.now()
    if time.month == 8 and time.day == 14:
        a = 'YES!'
    template = loader.get_template('independence.html')
    context = {
        'display': a,
    }
    return HttpResponse(template.render(context,request))