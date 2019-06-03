from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile


# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    return render(request, 'home.html')
