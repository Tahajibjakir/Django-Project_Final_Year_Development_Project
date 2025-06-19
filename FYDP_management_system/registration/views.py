from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def dashboard(request):
    return render(request,'registration/home.html')







def t_registration(request):
    if request.method=='POST':
       username=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       password2=request.POST.get("repassword")
       if password!=password2:
         return HttpResponse('password does not match')
       else:
           my_user=User.objects.create_user(username,email,password)
           my_user.save()
           return redirect('t_login')

    return render(request,'registration/teacher_registration.html')



def s_registration(request):
    if request.method=='POST':
       username=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       password2=request.POST.get("repassword")
       if password!=password2:
         return HttpResponse('password does not match')
       else:
           my_user=User.objects.create_user(username,email,password)
           my_user.save()
           return redirect('s_login')

    return render(request,'registration/student_registration.html')





def t_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('t_home')
        else:
            return HttpResponse('username or password is incorrect')



    return render(request,'registration/teacher_login.html')



def s_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('s_home')
        else:
            return HttpResponse('username or password is incorrect')


    return render(request,'registration/student_login.html')
