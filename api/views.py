
from django.shortcuts import get_object_or_404, redirect
from requests import Response
from rest_framework import viewsets
from .models import  *
from api.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authtoken.models import Token
#TODO check this
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
import requests
url='http://127.0.0.1:8000/api/'

def get_portfolio_id(id):
    """Cette fonction n'est pas nécessaire car on a déjà utilisé signals donc user id = portfolio id = profile id"""
    return portfolio.objects.get(usr=id)

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
 
@csrf_exempt            
@api_view(['GET', 'POST'])
#@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
def post_or_get_all_skills(request,id):
    if request.method=='POST':
        serializer=SkillSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=get_portfolio_id(id).pk)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        skills=skill.objects.filter(portoflio_id=id)
        if len(skills)==0:
            return Response(status=204)
        serializer=SkillSerializer(skills, context={'request': request}, many=True)
        return Response(serializer.data, status=200,content_type='application/json')
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,content_type='application/json')

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_formation(request,id):
    if request.method=='POST':
        serializer=FormationSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        formations=formation.objects.filter(portoflio_id=id)
        if len(formations)==0:
            return Response(status=204)
        serializer=FormationSerializer(formations, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_language(request,id):
    if request.method=='POST':
        serializer=LanguageSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        languages=language.objects.filter(portoflio_id=id)
        if len(languages)==0:
            return Response(status=204)
        serializer=LanguageSerializer(languages, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_social(request,id):
    if request.method=='POST':
        serializer=Social_accountsSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=social_accounts.objects.filter(portoflio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=Social_accountsSerializer(accounts, context={'request': request}, many=False)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_work(request,id):
    if request.method=='POST':
        serializer=Work_experienceSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=work_experience.objects.filter(portoflio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=Work_experienceSerializer(accounts, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_certif(request,id):
    if request.method=='POST':
        serializer=CertificateSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=certificate.objects.filter(portoflio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=CertificateSerializer(accounts, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_recom_letter(request,id):
    if request.method=='POST':
        serializer=RecommendationLetterSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=recommendationLetter.objects.filter(portoflio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=RecommendationLetterSerializer(accounts, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_motiv_letter(request,id):
    if request.method=='POST':
        serializer=MotivationLetterSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portfolio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=motivationLetter.objects.filter(portfolio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=MotivationLetterSerializer(accounts, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_volun(request,id):
    if request.method=='POST':
        serializer=VolunteeringSerializer(data=request.data)
        #serializer["portfolio"]=id
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=id)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        accounts=volunteering.objects.filter(portoflio_id=id)
        if len(accounts)==0:
            return Response(status=204)
        serializer=VolunteeringSerializer(accounts, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# not working
@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_pro_accomp(request,id):
    if request.method=='POST':
        serializer=ProfessionalAccomplishmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(portfolio_id=get_portfolio_id(id).pk)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        pro_acc=professionalAccomplishment.objects.filter(portfolio_id=get_portfolio_id(id).pk)
        if len(pro_acc)==0:
            return Response(status=204)
        serializer=ProfessionalAccomplishmentSerializer(pro_acc, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_projects(request,id):
    if request.method=='POST':
        serializer=ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(portoflio_id=get_portfolio_id(id).pk)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        pro_acc=project.objects.filter(portoflio_id=get_portfolio_id(id).pk)
        if len(pro_acc)==0:
            return Response(status=204)
        serializer=ProjectSerializer(pro_acc, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['GET', 'POST'])
def post_or_get_all_awards(request,id):
    if request.method=='POST':
        serializer=AwardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(portfolio_id=get_portfolio_id(id).pk)
        return Response(serializer.data, status=201)
    elif request.method=='GET':
        pro_acc=award.objects.filter(portfolio_id=get_portfolio_id(id).pk)
        if len(pro_acc)==0:
            return Response(status=204)
        serializer=AwardSerializer(pro_acc, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
    
class ProfessionalAccomplishmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = professionalAccomplishment.objects.all()
    serializer_class = ProfessionalAccomplishmentSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    
class ProjectviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = project.objects.all()
    serializer_class = ProjectSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
   
class FeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']   
    
class AwardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = award.objects.all()
    serializer_class = AwardSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']