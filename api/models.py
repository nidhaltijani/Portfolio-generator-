from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
"""
class person(models.Model):
    
    email=models.EmailField(default='name@xyz.com')
    password=models.CharField(default="",max_length=40)
    class Meta:
        abstract=True
"""

class user(AbstractUser):
   
    email=models.EmailField(default='name@xyz.com',unique=True)
    password=models.CharField(default="",max_length=40)
    username = models.CharField(default="",max_length=40)
    
    USERNAME_FIELD = 'email' # unique identifier.
    REQUIRED_FIELDS = ['username'] 
    #verif
    class Meta:
        db_table='user'
        
class profile(models.Model):
    usr=models.OneToOneField(user,on_delete=models.CASCADE)
    first_name=models.CharField(null=False,blank=False,default='',max_length=50)
    last_name=models.CharField(null=False,blank=False,default='',max_length=50)
    birthday=models.DateField(default=date(2000,1,1))
    #TODO add min length 8
    phone_number=models.PositiveIntegerField(default=99999999)  #,max_length=8
    photo=models.ImageField(upload_to='photos/users') 
    
    class Meta:
        db_table="profile"
    # two methods to redefine the relation between user and profile
    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(usr=instance)

    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
class portfolio(models.Model):
    philosophy_statement=models.CharField(default="", max_length=50)
    about=models.TextField(null=True,blank=True)
    usr=models.OneToOneField(user,on_delete=models.CASCADE)
    
    class Meta:
        db_table='portfolio'
    
    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            portfolio.objects.create(usr=instance)

    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        instance.portfolio.save()
    
class language(models.Model):
    class proficiency(models.TextChoices):
        lvl0=(0,'No Proficiency')
        lvl1=(1,'Elementary Proficiency')
        lvl2=(2,'Limited Working Proficiency')
        lvl3=(3,'Professional Working Proficiency')
        lvl4=(4,'Full Professional Proficiency')
        lvl5=(5,'Native / Bilingual Proficiency')
        
    name=models.CharField(max_length=100,default="")
    typeoflanguage=models.CharField(max_length=30,choices=proficiency.choices,default=proficiency.lvl0)
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='language'

class skill(models.Model):
    name=models.CharField(default="", max_length=50)
    tool=models.CharField(blank=True, max_length=50)
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='skill'
        
class formation(models.Model):
    name=models.CharField(default="", max_length=50)
    establishment=models.CharField(default="", max_length=50)
    #on va voir si on va la laisser ou pas 
    country_establishment=models.CharField(default="", max_length=50)
    start_date=models.DateField(default=date(2022,1,1))
    end_date=models.DateField(default=date(2023,1,1))
    #TODO link to doc or photo
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='formation'
        
class accomplishment(models.Model):
    title=models.CharField(default="", max_length=50)
    summary=models.CharField(default="",max_length=500)
    justification=models.FileField(upload_to='pro_accomp/justifications')
    date_a=models.DateField(default=date(2022,1,1))
    class Meta:
        abstract=True
        
class professionalAccomplishment(accomplishment):
    class accomplishmentCategories(models.TextChoices):
        advising=("advising",'Spirit category')
        partnering=('partnering','Pioneer category')
        examining=('examining','Commitment category')
    #TODO
    #tasks=
    #categories
    accomp_type=models.CharField(choices=accomplishmentCategories.choices,default=accomplishmentCategories.advising,max_length=100)
    portfolio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='professional_Accomplishment'
        
class award(accomplishment):
    class recognitionLevel(models.TextChoices):
        national=("nat","national recognition")
        international=('inter','international recognition')
    recognition=models.CharField(default=recognitionLevel.national, choices=recognitionLevel.choices,max_length=100)
    portfolio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='award'
    
       
class social_accounts(models.Model):
    facebook=models.CharField(max_length=500, default="")
    github=models.CharField(max_length=500, default="",blank=True)
    linkedin=models.CharField(max_length=500, default="")
    website=models.CharField(max_length=500, default="",blank=True)
    google=models.CharField(max_length=500, default="",blank=True)
    portoflio=models.OneToOneField(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='social_accounts'


class project(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    date_creation=models.CharField(max_length=100,default="")
    visual_demo=models.FileField(upload_to="Project/demo")
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='project'
        #TODO verbose plural
  
        
class certificate(models.Model):
    class certiftype(models.TextChoices):
        completion=('comp','completion')
        achievement=('ach','achievement')
        professional=('pro','professional')
    name=models.CharField(default="", max_length=50)
    organization=models.CharField(default="", max_length=50)
    certification_type=models.CharField(choices=certiftype.choices,default=certiftype.completion, max_length=50)
    
    #TODO link to doc or photo
    
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='certificate'
 
    
class volunteering(models.Model):
    poste=models.CharField(default="",max_length=50)
    organization=models.CharField(default="", max_length=50)
    start_date=models.DateField(default=date(2022,1,1))
    end_date=models.DateField(default=date(2022,1,1))
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='volunteering'
    pass


class work_experience(models.Model):
    poste=models.CharField(default="",max_length=50)
    organization=models.CharField(default="", max_length=50)
    start_date=models.DateField(default=date(2022,1,1))
    end_date=models.DateField(default=date(2022,1,1))
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table='work_experience'
 
    
class feedback(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    title=models.CharField(default="", max_length=50)
    feedback=models.CharField(default="", max_length=500)
    class Meta:
        db_table='feedback'


class letter(models.Model):
    letter=models.TextField(default="")
    date_of_letter=models.DateField(default=date(2022,1,1))
    class Meta:
        abstract=True


class motivationLetter(letter):
    portfolio=models.OneToOneField(portfolio,on_delete=models.CASCADE)
    class Meta:
        db_table="motivation_letter"


class recommendationLetter(letter):
    portoflio=models.ForeignKey(portfolio,on_delete=models.CASCADE)
    writer=models.CharField(default="", max_length=50)
    occupation=models.CharField(default="",max_length=50)
    class Meta:
        db_table='recommendation_letter'