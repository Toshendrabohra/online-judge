from django import forms
from django.forms.models import ModelForm
from .models import problemset,solutions,testcase

class UserSolution(ModelForm):
   # solution=forms.TField() 
    class Meta:
        model=solutions
        fields=['usersolution']
