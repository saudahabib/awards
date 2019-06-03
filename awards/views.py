from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Project, Rating


# Create your views here.
'''welcome view to process landing page'''
def welcome(request):
    projects = Project.objects.all()
    developers = Profile.objects.all()
    return render(request, 'home.html', {"projects":projects, "developers": developers})

def project(request, project_id):
    try:
        project = Projects.objects.get(id=article_id)
        projects = Project.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request, "single_project.html", {"project":project, "projects":projects})
