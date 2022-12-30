from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.http import HttpResponse
from .models import Quote
# Create your views here.

#hard coded quotes for when an actual db is not begin used
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

class QuoteListView(ListView):
    model = Quote
    template_name = 'quote/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'quotes'
    #ordering = ['-date_posted']

class QuoteDetailView(DetailView):
    model = Quote

class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    fields = ['author', 'content']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class QuoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Quote
    fields = ['author', 'content']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)
    
    # a function to only allow a user to update quotes they posted themselves
    def test_func(self):
        quote = self.get_object()
        if self.request.user == quote.poster:
            return True 
        return False

class QuoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Quote
    success_url = '/'

    # the same function: only allow the creator to delete the quote
    def test_func(self):
        quote = self.get_object()
        if self.request.user == quote.poster:
            return True 
        return False
    