from django import forms
from api.models import *


class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()
    
class signupForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()
    password2=forms.CharField()
    #username=forms.CharField(hidden=True)
    

    
class portfolioForm(forms.Form):
    philosophy_statement=forms.CharField()
    about=forms.CharField() #Charfield ?




"""class languageform(forms.Form):
    name=forms.CharField()
    typeoflanguage=forms.ChoiceField(choices=language.proficiency.choices)  # fazet l proficiency kifeh lhnee
    #user=forms.CharField()"""
    
    

class languageform(forms.Form):
    proficiency= [
    ('0','No Proficiency'),
    ('1','Elementary Proficiency'),
    ('2','Limited Working Proficiency'),
    ('3','Professional Working Proficiency'),
    ('4','Full Professional Proficiency'),
    ('5','Native / Bilingual Proficiency'),

]
    name=forms.CharField(label="name",max_length=200)
    typeoflanguage=forms.ChoiceField(widget=forms.RadioSelect,choices=proficiency)

class skillform(forms.Form):
    name=forms.CharField()
    tool=forms.CharField() 



class formationform(forms.Form):
    name=forms.CharField()
    establishment=forms.CharField() 
    country_establishment=forms.CharField()
    start_date=forms.DateField()
    end_date=forms.DateField()







class professionalAccomplishmentForm(forms.Form):
    accomplishmentCategories=[
    ("advising",'Spirit category'),
    ('partnering','Pioneer category'),
    ('examining','Commitment category'),
    ]
    title=forms.CharField()
    summary=forms.CharField() 
    justification=forms.FileField()
    date_a=forms.DateField()
    accomp_type=forms.MultipleChoiceField(widget=forms.RadioSelect,choices =accomplishmentCategories) 

    

class awardform(forms.Form):
    recognition=forms.CharField() #kikikiikf
 

class social_accounts_form(forms.Form):
    facebook=forms.CharField()
    github=forms.CharField() 
    linkedin=forms.CharField()
    website=forms.CharField()
    facebook=forms.CharField()
    google=forms.CharField() 


class project(forms.Form):
    name=forms.CharField()
    description=forms.CharField() 
    linkedate_creationdin=forms.DateField() #fl models mahtouta charfield nbadlouha ?
    visual_demo=forms.FileField()




class certificate(forms.Form):
    name=forms.CharField()
    organization=forms.CharField() 
    certification_type=forms.CharField() #enumération ya ghalya

   
class volunteering(forms.Form):
    poste=forms.CharField()
    organization=forms.CharField() 
    start_date=forms.DateField()
    end_date=forms.DateField()


class work_experience(forms.Form):
    poste=forms.CharField()
    organization=forms.CharField() 
    start_date=forms.DateField()
    end_date=forms.DateField()


class letter(forms.Form):
    letter=forms.CharField()
    date_of_letter=forms.DateField() 



class motivationLetter(forms.Form):
    pass #hay fergha hedhy khaterha elle hérite koll chay ml lettre kifh naamlouolha ??

class recommendationLetter(forms.Form):
    writer=forms.CharField()
    occupation=forms.CharField() 



class portform(forms.ModelForm):
    class Meta:
        model=portfolio
        exclude=["usr"]
        
class profileForm(forms.ModelForm):
    photo=forms.ImageField()
    class Meta:
        model=profile
        exclude=["usr"]
        widgets={'photo': forms.FileInput(attrs={'class': 'form-control'}),}
        

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        exclude=["user"]
        
    def save(self,owner, commit=True):
        instance = super(feedbackForm, self).save(commit=False)
        instance.user = owner 
        if commit:
            instance.save()
        return instance