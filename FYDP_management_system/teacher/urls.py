from django.urls import path
from . import views
from .views import  userProfile
urlpatterns = [
    path('t_home/', views.t_home,name='t_home'),
    
    path('work_area/', views.work_area,name='work_area'),
    path('edits/', views.userProfile,name='edits'),

    path('t_profile/', views.t_profile,name='t_profile'),
    path('t_logout/', views.t_logout,name='t_logout'),
    
    

]