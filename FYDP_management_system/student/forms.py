from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from student.models import S_Profile,Supervisor_selection
from django.forms import ModelForm


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model=S_Profile
        exclude=('user',)

class Supervisor_selectionForm(ModelForm):
    class Meta:
        model=Supervisor_selection
        fields='__all__'



