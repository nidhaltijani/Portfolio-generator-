
from requests import Response
from rest_framework import viewsets
from .models import  *
from api.serializers import *
from rest_framework.permissions import  IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
#TODO check this

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)




class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfileViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    

class PortfolioViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = portfolio.objects.all()
    serializer_class = PortfolioSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class LanguageViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = language.objects.all()
    serializer_class = LanguageSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class SkillViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = skill.objects.all()
    serializer_class = SkillSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class FormationViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = formation.objects.all()
    serializer_class = FormationSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfessionalAccomplishmentViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = professionalAccomplishment.objects.all()
    serializer_class = ProfessionalAccomplishmentSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class AwardViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = award.objects.all()
    serializer_class = AwardSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class Social_accountsViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = social_accounts.objects.all()
    serializer_class = Social_accountsSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProjectviewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = project.objects.all()
    serializer_class = ProjectSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class CertificateViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = certificate.objects.all()
    serializer_class = CertificateSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class VolunteeringViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = volunteering.objects.all()
    serializer_class = VolunteeringSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class Work_experienceViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = work_experience.objects.all()
    serializer_class = Work_experienceSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class FeedbackViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class MotivationLetterViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = motivationLetter.objects.all()
    serializer_class = MotivationLetterSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class RecommendationLetterViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    
    queryset = recommendationLetter.objects.all()
    serializer_class = RecommendationLetterSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    
    
