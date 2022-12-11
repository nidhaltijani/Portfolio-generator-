from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', my_profile,name="profile"),
    path('login/', signin,name="login"),
    path('about/', about,name="about"),
    path('logout/', logout,name="logout"),
    path('signup/', signup,name="signup"),
    path('acc/', create_accomplishment,name="signup"),
    path('award/', create_accomplishment,name="signup"),
    path('skill/', skill_view_create,name="skill"),
    path('skillget/', skills_get,name="skillget"),
    path('formationget/', formations_get,name="formationget"),
    path('formation/', formation_view_create,name="formation"),
    path('language/', language_view_create,name="language"),
    path('social/', social_view_create,name="social"),
  
    
    #path('oauth/', include('social_django.urls', namespace='social')),
]
