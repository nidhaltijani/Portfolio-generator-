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
    path('lang/', language_view_create,name="lang"),
    
    #path('oauth/', include('social_django.urls', namespace='social')),
]
