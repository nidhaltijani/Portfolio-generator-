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
from django.conf import settings
import os
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
            return redirect('signin')
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
                
                return redirect('index_connected')
            else :
                messages.error(request,'Invalid credentials!')
                #return redirect('login') # to signup view
                return render(request,'login.html',{'form':logform})
    else :
        logform = loginform()
        return render(request,'login.html',{'form':logform})

@login_required(login_url='signin') 
def logout(request):
    auth.logout(request)
    for key in request.session.keys():
        del request.session[key]
    return redirect('http://127.0.0.1:8000/app/')



#tekhdem
@login_required(login_url='signin') 
def about(request):
    porform=portfolioForm(request.POST or None)
    if porform.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        #res=requests.get(f'{url}portfolio/2/')
        response=requests.patch(f'{url}portfolio/{request.user.pk}/',data=porform.data,headers=header)
        return redirect('work')
    return render(request,"about.html",{"form":porform})
    

#@login_required(login_url='signin')
#enfin khedmet bel authentificationnnnnnnnn
#update profile

def simple_upload(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url
        
@login_required(login_url='signin') 
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
            return redirect('about') 
        
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
        return redirect('award')
     
    return render(request,'skill.html',{'skillform':language_f})



@login_required(login_url='signin')
def formation_view_create(request):   
    form=formationform(request.POST or None) #ne pas faire 2 instances du form
    
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}formation/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('skill')
    return render(request,'formation.html',{'form':form})


@login_required(login_url='signin')
def language_view_create(request):   
    form=languageform(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}language/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('certif')
    return render(request,'language.html',{'form':form})



@login_required(login_url='signin')
def social_view_create(request):   
    form=social_accounts_form(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}social/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('portfolio')
    return render(request,'social.html',{'form':form})

@login_required(login_url='signin')
def work_view_create(request):   
    form=work_experience(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}work/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('volunteering')
    return render(request,'work.html',{'form':form})

@login_required(login_url='signin')
def certif_view_create(request):   
    form=certificate(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}certif/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('social')
    return render(request,'certificates.html',{'form':form})

@login_required(login_url='signin')
def recom_view_create(request):   
    form=recommendationLetter(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}recom/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('language')
    return render(request,'recom_letter.html',{'form':form})

@login_required(login_url='signin')
def motiv_view_create(request):   
    form=motivationLetter(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}motiv/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('project')
    return render(request,'motivation_letter.html',{'form':form})

@login_required(login_url='signin')
def volunt_view_create(request):   
    form=volunteering(request.POST or None) #ne pas faire 2 instances du form
    if form.is_valid():
        header = {"Authorization": f"Token {request.session['token']}"}
        response=requests.post(f"{url}volunt/{request.user.pk}/",data=form.data,headers=header) 
        return redirect('formation')
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
           
            return redirect('motivation')
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
           
            return redirect('recom')
        return render(request,'project.html',{'form':form})
    form=projectForm()
    return render(request,'project.html',{'form':form})


@login_required(login_url='signin')
def award_view_create(request):  
    if request.method=='POST':
        form=awardform(request.POST) #ne pas faire 2 instances du form
        if form.is_valid():
            #photo_url=simple_upload(request)
            header = {"Authorization": f"Token {request.session['token']}"}
            response=requests.post(f"{url}award/{request.user.pk}/",data=form.data,headers=header) 
            """result=response.json()
            res=requests.patch(f"{url}awardview/{result['id']}/",data={"image_url":photo_url},headers=header) """
           
            return redirect('professional')
        return render(request,'award.html',{'form':form})
    form=awardform()
    return render(request,'award.html',{'form':form})

#get for portfolio display

@login_required(login_url='signin')
def skills_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}skill/{request.user.pk}/",headers=header) 
    #response.json()
    skills=None
    if response.status_code==200:
        skills=response.json()
    return skills


@login_required(login_url='signin')
def languages_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}language/{request.user.pk}/",headers=header) 
    languages=None
    if response.status_code==200:
        languages=response.json()
    return languages

@login_required(login_url='signin')
def formations_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}formation/{request.user.pk}/",headers=header) 
    formations=None
    if response.status_code==200:
        formations=response.json()
    return formations

@login_required(login_url='signin')
def socials_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}social/{request.user.pk}/",headers=header) 
    socials=None
    if response.status_code==200:
        socials=response.json()
    return socials


@login_required(login_url='signin')
def works_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}work/{request.user.pk}/",headers=header) 
    works=None
    if response.status_code==200:
        works=response.json()
    return works
 
@login_required(login_url='signin')
def certifs_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}certif/{request.user.pk}/",headers=header) 
    certifs=None
    if response.status_code==200:
        certifs=response.json()
    return certifs

@login_required(login_url='signin')
def recoms_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}recom/{request.user.pk}/",headers=header) 
    recoms=None 
    if response.status_code==200:
        recoms=response.json()
    return recoms

#feha probleme
@login_required(login_url='signin')
def motiv_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}motiv/{request.user.pk}/",headers=header) 
    motiv=None
    if response.status_code==200:
        motiv=response.json()
    return motiv 

@login_required(login_url='signin')
def volunts_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}volunt/{request.user.pk}/",headers=header) 
    volunts=None
    if response.status_code==200:
        volunts=response.json()
    return volunts 

@login_required(login_url='signin')
def profs_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}professional/{request.user.pk}/",headers=header) 
    profs=None
    if response.status_code==200:
        profs=response.json()
    return profs 

@login_required(login_url='signin')
def projects_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}proj/{request.user.pk}/",headers=header) 
    projects=None
    if response.status_code==200:
        projects=response.json()
    return projects 


@login_required(login_url='signin')
def awards_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}award/{request.user.pk}/",headers=header) 
    awards=None
    if response.status_code==200:
        awards=response.json()
    return awards 

@login_required(login_url='signin')
def portfolio_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}portfolio/{request.user.pk}/",headers=header) 
    portfolio=response.json()
    return portfolio 

@login_required(login_url='signin')
def profile_get(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.get(f"{url}profile/{request.user.pk}/",headers=header) 
    portfolio=response.json()
    return portfolio 

@login_required(login_url='signin') 
def display_portfolio(request):
    skills=skills_get(request)
    languages=languages_get(request)
    formations=formations_get(request)
    socials=socials_get(request)
    works=works_get(request)
    certifs=certifs_get(request)
    recoms=recoms_get(request)
    motivs=motiv_get(request)
    volunts=volunts_get(request)
    profs=profs_get(request)
    projects=projects_get(request)
    awards=awards_get(request)
    portfolio=portfolio_get(request)
    profile=profile_get(request)
    images=os.listdir(settings.MEDIA_ROOT)
   # age=get_age(request)
    
    recomform=recommendationLetter()
    context={"skills":skills,"languages":languages,"formations":formations,"socials":socials,"works":works,
             "certifs":certifs,"recoms":recoms,"volunts":volunts,"motivs":motivs,"profs":profs,"projects":projects,
             "awards":awards,"portfolio":portfolio,"profile":profile,"images":images,"recomform":recomform}
    if request.method=="POST":
        
        recomform=recommendationLetter(request.POST or None)
        if recomform.is_valid():
            header = {"Authorization": f"Token {request.session['token']}"}
            response=requests.post(f"{url}recom/{request.user.pk}/",data=recomform.data,headers=header) 
            return redirect("portfolio")
    return render(request,"portfolio.html",context)

@login_required(login_url='signin') 
def published(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    response=requests.patch(f"{url}portfolio/{request.user.pk}/",data={"is_published":True},headers=header) 
    return redirect("portfolio")

@login_required(login_url='signin') 
def get_feedbacks(request):
    header = {"Authorization": f"Token {request.session['token']}"}
    feedback1=requests.get(f"{url}feedbackview/1/",headers=header).json()
    feedback2=requests.get(f"{url}feedbackview/2/",headers=header).json() 
    feedback3=requests.get(f"{url}feedbackview/3/",headers=header).json() 
    return feedback1,feedback2,feedback3

def index(request):
    return render(request,"index.html")

@login_required(login_url="signin")
def index_connected(request):
    feedback1,feedback2,feedback3=get_feedbacks(request)
    return render(request,"index_connected.html",{"feedback1":feedback1,"feedback2":feedback2,"feedback3":feedback3})


@login_required(login_url='signin') 
def update_profile(request):
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
            return redirect('portfolio') 
        
        return render(request,'edit.html',{'profileform':profform})
    profile=profile_get(request) #to get default values
    profform=profileForm(initial=profile)
    return render(request,'edit.html',{'profileform':profform})