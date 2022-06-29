from django import forms
from django.forms.models import ModelForm
from .models import Problemset,Submission,Testcase

class UserSolution(ModelForm):
   # solution=forms.TField() 
    class Meta:
        model=Submission
        fields=['user_submission']
