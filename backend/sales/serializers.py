from rest_framework import serializers
from .models import Lead, Deal, Stage, Activity
from .services import LeadService, DealService, StageService, ActivityService


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'company', 'user', 'name', 'email', 'phone', 'status', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['company', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Chama o serviço para criar o Lead
        return LeadService.create_lead(validated_data)

    def update(self, instance, validated_data):
        # Chama o serviço para atualizar o Lead
        return LeadService.update_lead(instance, validated_data)


class DealSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)  # Representação do lead relacionado
    stage = serializers.CharField()  # Pode ser uma escolha de stage ou uma string
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    expected_close_date = serializers.DateField(allow_null=True, required=False)
    notes = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Deal
        fields = ['id', 'lead', 'company', 'stage', 'value', 'expected_close_date', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['company', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Chama o serviço para criar o Deal
        return DealService.create_deal(validated_data)

    def update(self, instance, validated_data):
        # Chama o serviço para atualizar o Deal
        return DealService.update_deal(instance.id, validated_data)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['id', 'name', 'order', 'company', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Chama o serviço para criar o Stage
        return StageService.create_stage(validated_data)

    def update(self, instance, validated_data):
        # Chama o serviço para atualizar o Stage
        return StageService.update_stage(instance, validated_data)


class ActivitySerializer(serializers.ModelSerializer):
    deal = DealSerializer(read_only=True)  # Representação do deal relacionado
    activity_type = serializers.CharField()  # Pode ser um campo com tipos específicos, ex.: 'call', 'meeting'
    description = serializers.CharField()
    user = serializers.StringRelatedField(read_only=True)  # Representação do usuário que registrou a atividade

    class Meta:
        model = Activity
        fields = ['id', 'deal', 'activity_type', 'description', 'user', 'date']
        read_only_fields = ['date']

    def create(self, validated_data):
        # Chama o serviço para criar a Activity
        return ActivityService.create_activity(validated_data)

    def update(self, instance, validated_data):
        # Chama o serviço para atualizar a Activity
        return ActivityService.update_activity(instance, validated_data)
