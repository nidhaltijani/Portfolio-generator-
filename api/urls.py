from django.urls import include,path
from rest_framework import routers
#from rest_framework_nested import routers
from .views import *
import rest_framework
#urls using ModelViewSet
router=routers.DefaultRouter() #get the default router object defined in rest_framework







#each time we use the path '/users' in the url, 
#the UserViewSet will be called
#the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)

#router.register(r'users',UserViewSet)  returns all users no need for it only for admin
#router.register(r'portfolio',PortfolioViewSet,basename="portfolio") 
router.register(r'profile',ProfileViewSet,basename="profile") 
router.register(r'portfolio',PortfolioViewSet) 
router.register(r'proview',ProfessionalAccomplishmentViewSet) 
router.register(r'projectview',ProjectviewSet) 
router.register(r'awardview',AwardViewSet) 




"""
router1=routers.SimpleRouter()
router1.register('portfolio',PortfolioViewSet,basename="portfolio")
portfolio_router=routers.NestedSimpleRouter(
    router1,
    r'usr',
    lookup='usr'
)

portfolio_router.register(
    r'books',
    views.BookViewSet,
    basename='library-book'
)
"""



#add the router to the urlpatterns
urlpatterns = [
     path('', include(router.urls)),
     path(r'auth/',login,name="user authentif API"),
     path(r'register/',signup,name="signup"),
     path(r'skill/<int:id>/',post_or_get_all_skills,name="skill"),
     path(r'formation/<int:id>/',post_or_get_all_formation,name="formation"),
     path(r'language/<int:id>/',post_or_get_all_language,name="language"),
     path(r'social/<int:id>/',post_or_get_all_social,name="social"),
     path(r'professional/<int:id>/',post_or_get_all_pro_accomp,name="pro_acc"),
     path(r'work/<int:id>/',post_or_get_all_work,name="work"),
     path(r'certif/<int:id>/',post_or_get_all_certif,name="certif"),
     path(r'recom/<int:id>/',post_or_get_all_recom_letter,name="recom"),
     path(r'motiv/<int:id>/',post_or_get_all_motiv_letter,name="motiv"),
     path(r'volunt/<int:id>/',post_or_get_all_volun,name="volunt"),
     path(r'proj/<int:id>/',post_or_get_all_projects,name="proj"),
     path(r'award/<int:id>/',post_or_get_all_awards,name="award"),
     
    # path('',include(user_router.urls)),
     #path(r'connect/',include("rest_framework.urls")),
    # path('try/', get_token,name="get"),
     
    
    
]