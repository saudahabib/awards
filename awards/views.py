from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Project, Rating
from .forms import RatingForm
from django.contrib.auth.decorators import login_required
# Create your views here.
'''welcome view to process landing page'''
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    developers = Profile.objects.all()
    return render(request, 'home.html', {"projects":projects, "developers": developers})

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        projects = Project.objects.all()
    except:
        raise Http404()
    return render(request, "single_project.html", {"project":project, "projects":projects})
