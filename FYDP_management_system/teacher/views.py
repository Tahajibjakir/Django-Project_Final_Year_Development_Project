from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserProfileForm
from .models import T_Profile
from django.contrib import messages
# Create your views here.

def t_home(request):
    return render(request,'teacher/t_home.html')

def work_area(request):
    return render(request,'teacher/work_area.html')
def t_profile(request):
    user=request.user
    return render(request,'teacher/t_profile.html',{'user':user})
def t_logout(request):
    logout(request)
    return redirect('t_login')

def userProfile(request):
    try:
        instance=T_Profile.objects.get(user=request.user)
    except T_Profile.DoesNotExist:
        instance=None

    if request.method=='POST':
        if instance:
            form=UserProfileForm(request.POST, request.FILES, instance=instance)
        else:
            form=UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'Successfully saved your profile!!')
            return redirect('t_home')
    else:
        form=UserProfileForm(instance=instance)
    context={
        'form':form
    }
    
    return render(request, 'teacher/edits.html', context)

