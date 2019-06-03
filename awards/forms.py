from django import forms
from .models import Project, Rating, Profile
class RatingForm(forms.Form):
    design=forms.IntegerField(label='Design')
    usability=forms.IntegerField(label='Usability')
    content=forms.IntegerField(label='Content')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [""]
