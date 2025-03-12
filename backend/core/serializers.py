from rest_framework import serializers
from core.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.cep = validated_data.get('cep', instance.cep)
        instance.code = validated_data.get('code', instance.code)
        instance.active = validated_data.get('active', instance.active)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance