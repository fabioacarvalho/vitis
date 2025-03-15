from rest_framework import serializers
from .models import CustomerSuccess, Engagement, SupportTicket, Task, CustomerFeedback
from clients.models import Client
from core.models import Company
from sales.models import Lead

class CustomerSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSuccess
        fields = ['id', 'client', 'company', 'nps_score', 'retention_rate', 'last_engaged']


class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = ['id', 'lead', 'customer_success', 'date', 'interaction_type', 'notes']


class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['id', 'client', 'company', 'created_at', 'resolved_at', 'issue_description', 'resolution_notes']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'customer_success', 'description', 'due_date', 'completed']


class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = ['id', 'client', 'company', 'feedback_date', 'feedback_text', 'feedback_type']
