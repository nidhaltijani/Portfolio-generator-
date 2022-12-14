from rest_framework import serializers
from .models import *

#on a créé 2 serialziers un pour user et un pour register pour ne pas rendre le pswrd lors
#dune requete get

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [ 'email', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields= [ 'email', 'username', 'password']
        # hide password
       
        extra_kwargs = {
            'password': {'write_only':True}
        }


    # hash passwords in the database, override default create function
    def create(self, validated_data):
        #either we use user.objects.create to hash pswrd orself.Meta.model(**validated_data) and use set_password method
        n=user.objects.count()
        n=str(n)
        usr = user.objects.create_user(n, validated_data['email'], validated_data['password'])
        return usr 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields='__all__'
class PortfolioSerializer(serializers.ModelSerializer):
    #usr=UserSerializer(many=False)
    class Meta:
        model=portfolio
        fields=['id','philosophy_statement','about','is_published'] #serializes all fields    


class LanguageSerializer(serializers.ModelSerializer):
    typesoflanguage=serializers.CharField(source='get_typeoflanguage_display',required=False,allow_blank=True) # to display the human readable version
    class Meta:
        model=language
        fields=["name","typeoflanguage","typesoflanguage"] #serializes all fields 
           


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields=['name','tool'] #serializes all fields    
    """def save(self, **kwargs):
        return super().save(**kwargs)"""


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model=formation
        fields=["name","establishment","country_establishment","start_date","end_date"] #serializes all fields  
        

class ProfessionalAccomplishmentSerializer(serializers.ModelSerializer):
    accompp_type=serializers.CharField(source='get_accomp_type_display',required=False,allow_blank=True) #did too much problems
    class Meta:
        model=professionalAccomplishment
        fields=["id","title","summary","photo","image_url","date_a","accomp_type","accompp_type"]
        


class AwardSerializer(serializers.ModelSerializer):
    recognitions=serializers.CharField(source='get_recognition_display',required=False,allow_blank=True)
    class Meta:
        model=award
        #fields=["recognition"] #serializes all fields    
        #exclude=["portfolio","photo"]
        fields=["id","title","summary","photo","image_url","date_a","recognition","recognitions"]

class Social_accountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=social_accounts
        fields=["facebook","github","linkedin","website","google"] #serializes all fields    
        


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields=["id","name","description","date_creation","visual_demo","image_url"] #serializes all fields  
         

class CertificateSerializer(serializers.ModelSerializer):
    certification_types=serializers.CharField(source='get_certification_type_display',required=False,allow_blank=True)
    class Meta:
        model=certificate
        #exclude=["portoflio"] #serializes all fields 
        fields=["name","organization","certification_type","certification_types"]
           


class VolunteeringSerializer(serializers.ModelSerializer):
    class Meta:
        model=volunteering
        fields=["poste","organization","start_date","end_date"] #serializes all fields    
        

class Work_experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=work_experience
        fields=["poste","organization","start_date","end_date"] #serializes all fields    
        


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=feedback
        fields=["title","feedback"] #serializes all fields    
       


class MotivationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=motivationLetter
        exclude=["portfolio"] #serializes all fields    


class RecommendationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=recommendationLetter
        exclude=["portoflio"] #serializes all fields    