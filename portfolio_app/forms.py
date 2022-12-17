from django import forms
from api.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class loginform(forms.Form):
    email=forms.EmailField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your email'}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'write your password'}))
    
class signupForm(forms.Form):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your email'}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'write your password'}))
    password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'rewrite your password'}))
    #username=forms.CharField(hidden=True)
    def is_valid(self) -> bool:
        valid= super().is_valid()
        if not valid or not (self.cleaned_data['password']==self.cleaned_data['password2']):
            return False
        return True

    
class portfolioForm(forms.Form):
    philosophy_statement=forms.CharField(required=True)
    about=forms.CharField(required=True) #Charfield ?




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
    name=forms.CharField(label="name",max_length=200,required=True)
    typeoflanguage=forms.ChoiceField(choices=proficiency)

class skillform(forms.Form):
    name=forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Skill'}))
    tool=forms.CharField() 



class formationform(forms.Form):
    name=forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    establishment=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'establishment name'})) 
    country_establishment=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}))
    start_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
)
    end_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)







class professionalAccomplishmentForm(forms.Form):
    accomplishmentCategories=[
    ("advising",'Spirit category'),
    ('partnering','Pioneer category'),
    ('examining','Commitment category'),
    ]
    title=forms.CharField()
    summary=forms.CharField() 
    photo=forms.FileField() #changed last
    date_a=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    accomp_type=forms.ChoiceField(choices =accomplishmentCategories) 

    

class awardform(forms.Form):
    recog=[("nat","national recognition"),('inter','international recognition')]
    title=forms.CharField()
    summary=forms.CharField() 
    #photo=forms.FileField(required=False)
    date_a=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    recognition=forms.ChoiceField(choices=recog)
 

class social_accounts_form(forms.Form):
    facebook=forms.CharField()
    github=forms.CharField() 
    linkedin=forms.CharField()
    website=forms.CharField()
    #facebook=forms.CharField()
    google=forms.CharField() 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('facebook', css_class='form-group col-md-6 mb-0'),
                Column('github', css_class='form-group col-md-6 mb-0'),
                Column('linkedin', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('wesite', css_class='form-group col-md-6 mb-0'),
                Column('google', css_class='form-group col-md-4 mb-0'),
                #Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            #'check_me_out',
            Submit('submit', 'next')
        )


class projectForm(forms.Form):
    name=forms.CharField()
    description=forms.CharField() 
    date_creation=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),) #fl models mahtouta charfield nbadlouha ?
    #visual_demo=forms.FileField()
    photo=forms.FileField()
    


class certificate(forms.Form):
    certif_types=[('comp','completion'),
        ('ach','achievement'),
        ('pro','professional')]
    name=forms.CharField()
    organization=forms.CharField() 
    certification_type=forms.ChoiceField(choices=certif_types) #enumération ya ghalya

   
class volunteering(forms.Form):
    poste=forms.CharField()
    organization=forms.CharField() 
    start_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    end_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)


class work_experience(forms.Form):
    poste=forms.CharField()
    organization=forms.CharField() 
    start_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    end_date=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)


class letter(forms.Form):
    letter=forms.CharField()
    date_of_letter=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),) 
    


class motivationLetter(forms.Form):
    letter=forms.CharField(widget=forms.TextInput())
    date_of_letter=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    
class recommendationLetter(forms.Form):
    writer=forms.CharField(widget = forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Writer'
                }),)
    occupation=forms.CharField(widget = forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Occupation'
                }),) 
    date_of_letter=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    letter=forms.CharField(widget=forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 1300px;',
                'placeholder': 'Letter'
                }),)
   
    



class portform(forms.ModelForm):
    class Meta:
        model=portfolio
        exclude=["usr"]
        
class profileForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    birthday=forms.DateField(widget = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date',
               'style': 'width: 510px;height: 30px;',
              
               
              
              }),)
    #TODO add min length 8
    phone_number=forms.IntegerField()  #,max_length=8
    photo=forms.ImageField()
    occupation=forms.CharField()
    class Meta:
      
        widgets={'photo': forms.FileInput(attrs={'class': 'form-control'}),'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 510px;height: 30px;', 'class': 'form-control'})}
        
    def is_valid(self) -> bool:
        valid= super().is_valid()    
        if not self.cleaned_data['first_name'].isalpha():
            self.add_error('first_name', "first name must be only alphabetic")
            return False 
        if not self.cleaned_data['last_name'].isalpha():
            self.add_error('last_name', "last name must be only alphabetic")
            return False 
        if not (len(str(self.cleaned_data['phone_number']))==8):
            self.add_error('phone_number', "Phone number must be of length 8")
            return False  
        if not str(self.cleaned_data['phone_number'])[0] in ("2","9","5"):
            self.add_error('phone_number', "Phone number must start with 5 ,2 or 9")
            return False  
        return True
    

class feedbackForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    feedback=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Feedback', 'style': 'width: 300px;', 'class': 'form-control','rows': 4}))
    class Meta:
        model=feedback
        exclude=["user"]
        
        
    def save(self,owner, commit=True):
        instance = super(feedbackForm, self).save(commit=False)
        instance.user = owner 
        if commit:
            instance.save()
        return instance
    
class publishForm(forms.Form):
    pass