
from django.shortcuts import get_object_or_404, redirect
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
from rest_framework import status
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
    #redirect("profile")
    #user_id=user.objects.filter(email=email)
    #portfolio_id=portfolio.objects.get_or_create(usr=user_id)
    #,"user_id":user_id,"portfolio_id":portfolio_id
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
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    if request.method=='POST':
        email = request.data.get("email")
        password = request.data.get("password")
        password2 = request.data.get("password2")
        
        if password==password2:
            if user.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
                        #status)
                
            else :
                serializer = RegisterSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)   #if anything not valid, raise exception
                serializer.save()
                
                return Response({'success': "Account createdd succesfully"})
                  #  status=HTTP) # tnajem taamel moshkla khatr nafsha byn signup w login
               
        else :
            return Response({'error': 'Password doesnt match'})
            
@api_view(['GET', 'POST'])
def post_or_get_all_skills(request,id):
    if request.method=='POST':
        serializer=SkillSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        skills=skill.objects.filter(portoflio_id=id)
        if len(skills)==0:
            return Response(status=204)
        serializer=SkillSerializer(skills, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#get working



class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    #queryset = profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #username = self.kwargs['username']
        return profile.objects.filter(usr__id=self.request.user.pk)
    
class PortfolioViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = portfolio.objects.all()
    serializer_class = PortfolioSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    
class LanguageViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = language.objects.all()
    serializer_class = LanguageSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class SkillViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = skill.objects.all()
    serializer_class = SkillSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class FormationViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = formation.objects.all()
    serializer_class = FormationSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfessionalAccomplishmentViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = professionalAccomplishment.objects.all()
    serializer_class = ProfessionalAccomplishmentSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class AwardViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = award.objects.all()
    serializer_class = AwardSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class Social_accountsViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = social_accounts.objects.all()
    serializer_class = Social_accountsSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProjectviewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = project.objects.all()
    serializer_class = ProjectSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class CertificateViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = certificate.objects.all()
    serializer_class = CertificateSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class VolunteeringViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = volunteering.objects.all()
    serializer_class = VolunteeringSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class Work_experienceViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = work_experience.objects.all()
    serializer_class = Work_experienceSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class FeedbackViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class MotivationLetterViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = motivationLetter.objects.all()
    serializer_class = MotivationLetterSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class RecommendationLetterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    queryset = recommendationLetter.objects.all()
    serializer_class = RecommendationLetterSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

@api_view(["GET"])
def get_accomp_by_user_id(request,id):
    accomp=accomplishment.objects.filter(user=id)
    return Response(accomp)

def accomp_details_or_update_or_delete(request, pk):
    accom=get_object_or_404(accomplishment, user=pk)
    if request.method=='GET':
        serializer = ProfessionalAccomplishmentSerializer(accom, context={'request': request})
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ProfessionalAccomplishmentSerializer(accom, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        accom.delete()
        return Response(status=200)
    return Response(status=405)