
from requests import Response
from rest_framework import viewsets
from .models import  *
from api.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
#TODO check this
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
import requests
url='http://127.0.0.1:8000/api/'

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
"""
class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfileViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
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
    
    
