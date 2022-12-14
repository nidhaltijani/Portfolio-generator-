from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('profile/', my_profile,name="profile"),
    path('login/', signin,name="signin"),
    path('about/', about,name="about"),
    path('logout/', logout,name="logout"),
    path('signup/', signup,name="signup"),
    #path('acc/', create_accomplishment,name="signup"),
    #path('award/', create_accomplishment,name="signup"),
    path('skill/', skill_view_create,name="skill"),# apartir d'ici temshy
    path('skillget/', skills_get,name="skillget"),
    path('formationget/', formations_get,name="formationget"),
    path('formation/', formation_view_create,name="formation"),
    path('language/', language_view_create,name="language"),
    path('social/', social_view_create,name="social"),
    path('work/', work_view_create,name="work"),
    path('certificate/', certif_view_create,name="certif"),
    path('recommendation/', recom_view_create,name="recom"),
    path('professional/',pro_view_create,name="professional"), # not working
    path('motivation/',motiv_view_create,name="motivation"), # not working
    path('volunteering/',volunt_view_create,name="volunteering"), # not working
    path('project/',project_view_create,name="project"), # not working
    path('award/',award_view_create,name="award"), # not working
    path('portfolio/',display_portfolio,name="portfolio"), # not working
    path('',index,name="index"), # not working
    path('index/',index_connected,name="index_connected"), # not working
    path('feedback/',provide_feedback,name="feedback"), # not working
  
    
    #path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)