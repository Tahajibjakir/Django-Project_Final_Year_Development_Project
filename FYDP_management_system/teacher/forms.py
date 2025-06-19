from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from teacher.models import T_Profile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model=T_Profile
        exclude=('user',)
