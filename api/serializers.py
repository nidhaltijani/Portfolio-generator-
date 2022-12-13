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
        fields=['philosophy_statement','about'] #serializes all fields    


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=language
        fields=["name","typeoflanguage"] #serializes all fields    


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
    class Meta:
        model=professionalAccomplishment
        exclude=["portfolio",]  


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model=award
        #fields=["recognition"] #serializes all fields    
        exclude=["portfolio","photo"]

class Social_accountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=social_accounts
        fields=["facebook","github","linkedin","website","google"] #serializes all fields    
        


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields=["id","name","description","date_creation","visual_demo","image_url"] #serializes all fields  
         

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=certificate
        exclude=["portoflio"] #serializes all fields    


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