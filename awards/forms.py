from django import forms

class RatingForm(forms.Form):
    design=forms.IntegerField(label='Design')
    usability=forms.IntegerField(label='Usability')
    content=forms.IntegerField(label='Content')
