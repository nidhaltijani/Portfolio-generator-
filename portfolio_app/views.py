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
from django.core.files.storage import FileSystemStorage
# Create your views here.
#register is working perfectly


url='http://127.0.0.1:8000/api/'


#portfolio_id == user id cuz creation same time  with signals

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

def simple_upload(request):
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url
        

def my_profile(request):
    #user_profile=request.user
    if request.method=='POST':
        profform=profileForm(request.POST,request.FILES) #nahyna user_profile w hatyna 1 pour tester
        if profform.is_valid():
        #if request.method=='POST':
            photo_url=simple_upload(request)
            header = {"Authorization": f"Token {request.session['token']}"}
            #response=requests.delete(f'{url}profile/1/') #workssssssssss
            response=requests.patch(f"{url}profile/{request.user.pk}/",data=profform.data,headers=header) #profile id = user id
            res=requests.patch(f"{url}profile/{request.user.pk}/",data={"image_url":photo_url},headers=header)
            redirect('profile') 
        
        return render(request,'profileForm.html',{'profileform':profform})
    profform=profileForm()
    return render(request,'profileForm.html',{'profileform':profform})


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

@login_required(login_url='signin')
def skill_view_create(request):   
    language_f=skillform(request.POST or None) #ne pas faire 2 instances du form
    
    if language_f.is_valid():
        #post_data=language_f.data
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}skill/{request.user.pk}/",data=language_f.data,headers=header) 
        return redirect('login')
     
    return render(request,'skill.html',{'skillform':language_f})

@login_required(login_url='signin')
def skills_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}skill/{request.user.pk}/",headers=header) 
    #response.json()
    skills=response.json()
    
    return render(request,'skill.html',{"response":skills})


@login_required(login_url='signin')
def formation_view_create(request):   
    form=formationform(request.POST or None) #ne pas faire 2 instances du form
    
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}formation/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'formation.html',{'form':form})

@login_required(login_url='signin')
def formations_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}formation/{request.user.pk}/",headers=header) 
    return render(request,'formation.html')
    
@login_required(login_url='signin')
def language_view_create(request):   
    form=languageform(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}language/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'language.html',{'form':form})

@login_required(login_url='signin')
def languages_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}language/{request.user.pk}/",headers=header) 
    return render(request,'language.html')

@login_required(login_url='signin')
def social_view_create(request):   
    form=social_accounts_form(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}social/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'social.html',{'form':form})

@login_required(login_url='signin')
def work_view_create(request):   
    form=work_experience(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}work/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'work.html',{'form':form})

@login_required(login_url='signin')
def certif_view_create(request):   
    form=certificate(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}certif/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'certificates.html',{'form':form})

@login_required(login_url='signin')
def recom_view_create(request):   
    form=recommendationLetter(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}recom/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'recom_letter.html',{'form':form})

@login_required(login_url='signin')
def motiv_view_create(request):   
    form=motivationLetter(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}motiv/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'motivation_letter.html',{'form':form})

@login_required(login_url='signin')
def volunt_view_create(request):   
    form=volunteering(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}volunt/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('login')
    return render(request,'volunteering.html',{'form':form})


@login_required(login_url='signin')
def pro_view_create(request):  
    if request.method=='POST':
        form=professionalAccomplishmentForm(request.POST,request.FILES) #ne pas faire 2 instances du form
        if form.is_valid():
            photo_url=simple_upload(request)
            header = {"Authorization": f"Token {request.session['token']}"}
            response=requests.post(f"{url}professional/{request.user.pk}/",data=form.data,headers=header) 
            result=response.json()
            res=requests.patch(f"{url}proview/{result['id']}/",data={"image_url":photo_url},headers=header) 
           
            return redirect('login')
        return render(request,'ProAccomp.html',{'form':form})
    form=professionalAccomplishmentForm()
    return render(request,'ProAccomp.html',{'form':form})

@login_required(login_url='signin')
def project_view_create(request):  
    if request.method=='POST':
        form=projectForm(request.POST,request.FILES) #ne pas faire 2 instances du form
        if form.is_valid():
            photo_url=simple_upload(request)
            header = {"Authorization": f"Token {request.session['token']}"}
            response=requests.post(f"{url}proj/{request.user.pk}/",data=form.data,headers=header) 
            result=response.json()
            res=requests.patch(f"{url}projectview/{result['id']}/",data={"image_url":photo_url},headers=header) 
           
            return redirect('login')
        return render(request,'project.html',{'form':form})
    form=projectForm()
    return render(request,'project.html',{'form':form})