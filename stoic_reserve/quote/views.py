from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
# Create your views here.

quotes = [
    {
        'author': 'Carl Jung',
        'content': 'You are what you do, not what you say you will do.',
        'description': 'Honestly this quotes goes hard fr fr ong',
        'extraction': 'The Stoic Reader',
        'category': 'Philosophy'
    }, 
    {
        'author': 'Seneca',
        'content': 'If a man knows not to which port he sails, no wind is favorable.',
        'description': 'Honestly this quotes goes hard fr fr ong',
        'extraction': 'Letters from a Stoic',
        'category': 'Philosophy'
    }
]

def home(request):
    context = {
        'quotes': Quote.objects.all()
    }
    return render(request, 'quote/home.html', context)

def about(request):
    return render(request, 'quote/about.html')