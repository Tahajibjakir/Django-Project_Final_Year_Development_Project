from django.urls import path
from . import views
#from django.conf.urls.static import static
#from django.conf import settings
urlpatterns = [
    path('s_home/', views.s_home,name='s_home'),
    path('s_profile/', views.s_profile,name='s_profile'),
    path('supervisor/', views.supervisor,name='supervisor'),
    path('s_logout/', views.s_logout,name='s_logout'),
    path('s_edits/', views.s_edits,name='s_edits'),
]

#urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)