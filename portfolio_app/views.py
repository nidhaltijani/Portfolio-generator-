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


# not working
def signup(request):
    
        signform = signupForm(request.POST or None)
        res=""
        if signform.is_valid():
            res=requests.post(f'{url}register/',data=signform.data)
            redirect('login')
        return render(request,'signup.html',{"form":signform,"response":res})


def signin(request):
    if request.method=='POST':
        logform = loginform(request.POST)
        if logform.is_valid():
            email=logform.cleaned_data.get("email")
            password=logform.cleaned_data.get("password")
            usr=auth.authenticate(email=email,password=password)
            if usr is not None:
                auth.login(request,usr)
                response=requests.post(f"{url}auth/",data={"email":email,"password":password}) #json only uses double quotes
                request.session['token']=response.json()["token"]
                
                return redirect('about')
            else :
                messages.error(request,'Invalid credentials!')
                #return redirect('login') # to signup view
                return render(request,'login.html',{'form':logform})
    else :
        logform = loginform()
        return render(request,'login.html',{'form':logform})

@login_required(login_url='login') 
def logout(request):
    auth.logout(request)
    for key in request.session.keys():
        del request.session[key]
    return redirect('login')



#tekhdem
@login_required(login_url='login') 
def about(request):
    porform=portfolioForm(request.POST or None)
    if porform.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        #res=requests.get(f'{url}portfolio/2/')
        response=requests.patch(f'{url}portfolio/{request.user.pk}/',data=porform.data,headers=header)
        return redirect('login')
    return render(request,"about.html",{"form":porform})
    

#@login_required(login_url='signin')
#enfin khedmet bel authentificationnnnnnnnn
#update profile
def my_profile(request):
    #user_profile=request.user
    
    profform=profileForm(request.POST,request.FILES or None) #nahyna user_profile w hatyna 1 pour tester
    if profform.is_valid():
    #if request.method=='POST':
        header = {"Authorization": f"Token {request.session['token']}"}
        #response=requests.delete(f'{url}profile/1/') #workssssssssss
        response=requests.patch(f"{url}profile/{request.user.pk}/",data=profform.data,headers=header) #khdem zedaaaa
        redirect('profile')
    
       
            
       
    return render(request,'create_certif.html',{'user': 1,'profileform':profform})


#hehdy tekhdeeem 
def create_accomplishment(request):
    response=requests.get(f'{url}accomp/{request.user.pk}')
    return redirect('login')

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


def skill_view_create(request):   
    language_f=skillform(request.POST or None) #ne pas faire 2 instances du form
    
    if language_f.is_valid():
        #post_data=language_f.data
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}skill/{request.user.pk}/",data=language_f.data,headers=header) 
        redirect('login')
     
    return render(request,'skill.html',{'skillform':language_f})

def skills_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}skill/{request.user.pk}/",headers=header) 
    return render(request,'skill.html')
    

