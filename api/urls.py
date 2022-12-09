from django.urls import include,path
from rest_framework import routers
from .views import *
#urls using ModelViewSet
router=routers.DefaultRouter() #get the default router object defined in rest_framework






router.register(r'users',UserViewSet) 
#each time we use the path '/users' in the url, 
#the UserViewSet will be called
#the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)

#router.register(r'users',UserViewSet)  returns all users no need for it only for admin
router.register(r'portfolios',PortfolioViewSet) 
router.register(r'profile',ProfileViewSet,basename="profile") 
router.register(r'Languages',LanguageViewSet) 
router.register(r'skills',SkillViewSet) 
router.register(r'formations',FormationViewSet) 
router.register(r'ProfessionalAccomplishments',ProfessionalAccomplishmentViewSet) 
router.register(r'awards',AwardViewSet) 
router.register(r'SocialAccounts',Social_accountsViewSet) 
router.register(r'projects',ProjectviewSet) 
router.register(r'certifications',CertificateViewSet) 
router.register(r'Volunteering',VolunteeringViewSet) 
router.register(r'Work_experiences',Work_experienceViewSet) 
router.register(r'Motivation_Letter',MotivationLetterViewSet) 
router.register(r'Recommendation_Letters',RecommendationLetterViewSet) 


#add the router to the urlpatterns
urlpatterns = [
     path('', include(router.urls)),
     path(r'auth/', UserAuthentication.as_view(),name="user authentif API"),
     
    
    
]