
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('registration/',include('registration.urls')),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),

      

]
