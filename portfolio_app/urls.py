from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', my_profile,name="profile"),
    #path('oauth/', include('social_django.urls', namespace='social')),
]
