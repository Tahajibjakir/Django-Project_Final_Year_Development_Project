from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserProfileForm,Supervisor_selectionForm
from .models import S_Profile,Supervisor_selection


from django.contrib import messages
# Create your views here.
def s_home(request):
    form=Supervisor_selectionForm 
    if request.method=='POST':
       Sup_selectionForm =Supervisor_selectionForm(request.POST)
       if Sup_selectionForm.is_valid():
          Sup_selectionForm.save()
          messages.success(request,'Successfully saved your choice!!')
          return redirect('s_home')
        
    context1={
       'form':form
    }
   
    return render(request,'student/s_home.html',context1)




def s_profile(request):
    user=request.user
    return render(request,'student/s_profile.html',{'user':user})
def supervisor(request):
    return render(request,'student/supervisor.html')

def s_logout(request):
    logout(request)
    return redirect('s_login')

def s_edits(request):
    try:
        instance=S_Profile.objects.get(user=request.user)
    except S_Profile.DoesNotExist:
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
            return redirect('s_home')
    else:
        form=UserProfileForm(instance=instance)
    context={
        'form':form
    }
    
    return render(request, 'student/s_edits.html', context)