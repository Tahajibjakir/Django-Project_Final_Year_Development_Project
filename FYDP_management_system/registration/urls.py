from django.urls import path
from . import views
urlpatterns = [
        path('dashboard/', views.dashboard,name='dashboard'),
        
        path('t_registration/', views.t_registration, name='t_registration'),
        path('s_registration/', views.s_registration, name='s_registration'),
        path('t_login/', views.t_login,name='t_login'),
        path('s_login/', views.s_login,name='s_login'),



]