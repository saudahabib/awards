from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Profile
from .forms import NewPostForm, NewsProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    return render(request, 'home.html')
