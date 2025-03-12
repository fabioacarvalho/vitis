from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CompanyUser, CompanyInvitation
from core.models import Company


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['company_id'] = user.company.id if user.company else None
        token['role'] = user.role
        return token


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = ('username', 'password',)


class CompanyUserSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    
    class Meta:
        model = CompanyUser
        fields = ('id', 'username', 'email', 'role', 'company', 'is_company_admin')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CompanyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'user'),
            company=validated_data['company']
        )
        return user


class CompanyInvitationSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.nome', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = CompanyInvitation
        fields = [
            'id',
            'email',
            'company',
            'company_name',
            'created_by',
            'created_by_username',
            'created_at',
            'accepted',
            'token'
        ]
        extra_kwargs = {
            'token': {'read_only': True},
            'created_by': {'read_only': True},
            'company': {'write_only': True}
        }
    
    def validate_email(self, value):
        """Verifica se o email já foi convidado"""
        if CompanyInvitation.objects.filter(email=value, company=self.context['request'].user.company).exists():
            raise serializers.ValidationError("Este email já foi convidado para a empresa")
        return value
