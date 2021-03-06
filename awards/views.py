from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Project, Rating
from .forms import RatingForm, NewProjectForm
from django.contrib.auth.decorators import login_required
import random
# Create your views here.
'''welcome view to process landing page'''
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    developers = Profile.objects.all()
    number = random.randrange(10)
    return render(request, 'home.html', {"projects":projects, "developers": developers, "random":number})

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        projects = Project.objects.all()
    except:
        raise Http404()
    return render(request, "single_project.html", {"project":project, "projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user.id
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = Profile(current_user
            )
            project.save()
        return redirect('welcome')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form":form})
