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
    usr=UserSerializer(many=False)
    class Meta:
        model=portfolio
        fields=['philosophy_statement','about','usr'] #serializes all fields    


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=language
        fields='__all__' #serializes all fields    


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields='__all__' #serializes all fields    


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model=formation
        fields='__all__' #serializes all fields    


class ProfessionalAccomplishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=professionalAccomplishment
        fields='__all__' #serializes all fields    


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model=award
        fields='__all__' #serializes all fields    


class Social_accountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=social_accounts
        fields='__all__' #serializes all fields    


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields='__all__' #serializes all fields    


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=certificate
        fields='__all__' #serializes all fields    


class VolunteeringSerializer(serializers.ModelSerializer):
    class Meta:
        model=volunteering
        fields='__all__' #serializes all fields    


class Work_experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=work_experience
        fields='__all__' #serializes all fields    


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=feedback
        fields='__all__' #serializes all fields    


class MotivationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=motivationLetter
        fields='__all__' #serializes all fields    


class RecommendationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=recommendationLetter
        fields='__all__' #serializes all fields    