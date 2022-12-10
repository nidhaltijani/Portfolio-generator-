from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import user
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib import messages
from rest_framework.renderers import TemplateHTMLRenderer
from api.serializers import *
import requests
#login form 
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
# Create your views here.
#register is working perfectly


url='http://127.0.0.1:8000/api/'


def signup(request):
    if request.method=='POST':
        signform = signupForm(request.POST)
        if signform.is_valid():
            email=signform.cleaned_data.get("email")
            password=signform.cleaned_data.get("password")
            password2=signform.cleaned_data.get("password2")
            if password==password2:
                if user.objects.filter(email=email).exists():
                    messages.info(request,'email already taken')
                    return redirect('signup')
                else :
                    serializer = RegisterSerializer(data=signform.cleaned_data)
                    serializer.is_valid(raise_exception=True)   #if anything not valid, raise exception
                    serializer.save()
                    logform = loginform()
                    messages.info(request,'account created successfully') # tnajem taamel moshkla khatr nafsha byn signup w login
                    return redirect('signin')
            else :
                messages.info(request,'Password doesnt match')
                return redirect('signup') # to signup view
    else :
        signform=signupForm()
        return render(request,'signup.html',{"form":signform})



def signin(request):
    if request.method=='POST':
        logform = loginform(request.POST)
        if logform.is_valid():
            email=logform.cleaned_data.get("email")
            password=logform.cleaned_data.get("password")
            usr=auth.authenticate(email=email,password=password)
            if usr is not None:
                auth.login(request,usr)
                return redirect('/portfolio')
            else :
                messages.info(request,'Invalid credentials!')
                return redirect('signin') # to signup view
    else :
        logform = loginform()
        return render(request,'login.html',{'form':loginform})
   
   
    
@login_required(login_url='signin') 
def logout(request):
    auth.logout(request)
    return redirect('signin')

def get_token(): # problem hereee
    response=requests.post(f"{url}auth/",data={"email":"last@last.last","password":"last"}) #json only uses double quotes
    return response.json()["token"] # we should only take the tokennnn
    #return HttpResponse(response.text)

#@login_required(login_url='signin')
#enfin khedmet bel authentificationnnnnnnnn
def my_profile(request):
    #user_profile=request.user
    
    profform=profileForm(request.POST,request.FILES or None) #nahyna user_profile w hatyna 1 pour tester
    
    if request.method=='POST':
        header = {"Authorization": f"Token {get_token()}"}
        #response=requests.delete(f'{url}profile/1/') #workssssssssss
        response=requests.patch(f"{url}profile/2/",data=profform.data,headers=header) #khdem zedaaaa
        redirect('profile')
    
       
            
       
    return render(request,'create_certif.html',{'user': 1,'profileform':profform})


#hehdy tekhdeeem 

@login_required(login_url='signin')
def create_update_delete(request):
    user_profile = portfolio.objects.get(usr=request.user)
    portfo=portform()
    if request.method=='POST':
        portfo=portform(request.POST,instance=user_profile)
        if portfo.is_valid():
            portfo.save()
            return redirect('portfol')
        return render(request,'portfolio.html',{'user': user_profile,'portfo':portfo})
    return render(request,'portfolio.html',{'user': user_profile,'portfo':portfo})


@login_required(login_url='signin')
def provide_feedback(request):
    user_profile = request.user
    #fbk=feedback.objects.create(user=user_profile)
    fbkform=feedbackForm()
    if request.method=='POST':
        fbkform=feedbackForm(request.POST)
        if fbkform.is_valid():
            fbkform.save(owner=user_profile)
            return redirect('feedback')
        return render(request,'feedback.html',{'user': user_profile,'feedback':fbkform})
    return render(request,'feedback.html',{'user': user_profile,'feedback':fbkform})