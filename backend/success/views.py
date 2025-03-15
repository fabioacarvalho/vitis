from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from sales.models import Lead
from .models import CustomerSuccess, Engagement, SupportTicket, Task, CustomerFeedback
from .serializers import CustomerSuccessSerializer, EngagementSerializer, SupportTicketSerializer, TaskSerializer, CustomerFeedbackSerializer
from .services import (
    create_customer_success, 
    create_engagement, 
    create_support_ticket, 
    create_task, 
    create_customer_feedback, 
    resolve_support_ticket, 
    complete_task
)
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsCompanyUser

# ViewSet para CustomerSuccess
class CustomerSuccessViewSet(viewsets.ModelViewSet):
    queryset = CustomerSuccess.objects.all()
    serializer_class = CustomerSuccessSerializer
    permission_classes = [IsAuthenticated, IsCompanyUser]

    def create(self, request, *args, **kwargs):
        client = request.data.get('client')
        company = request.data.get('company')
        nps_score = request.data.get('nps_score')
        retention_rate = request.data.get('retention_rate')
        
        customer_success = create_customer_success(client, company, nps_score, retention_rate)
        serializer = self.get_serializer(customer_success)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def engagements(self, request, pk=None):
        customer_success = self.get_object()
        engagements = Engagement.objects.filter(customer_success=customer_success)
        serializer = EngagementSerializer(engagements, many=True)
        return Response(serializer.data)

# ViewSet para Engagement
class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = [IsAuthenticated, IsCompanyUser]

    def create(self, request, *args, **kwargs):
        customer_success_id = request.data.get('customer_success')
        lead_id = request.data.get('lead', None)
        interaction_type = request.data.get('interaction_type')
        notes = request.data.get('notes')

        customer_success = CustomerSuccess.objects.get(id=customer_success_id)
        lead = Lead.objects.get(id=lead_id) if lead_id else None
        engagement = create_engagement(customer_success, interaction_type, notes, lead)
        serializer = self.get_serializer(engagement)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ViewSet para SupportTicket
class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [IsAuthenticated, IsCompanyUser]

    def create(self, request, *args, **kwargs):
        client = request.data.get('client')
        company = request.data.get('company')
        issue_description = request.data.get('issue_description')
        resolution_notes = request.data.get('resolution_notes', None)
        
        support_ticket = create_support_ticket(client, company, issue_description, resolution_notes)
        serializer = self.get_serializer(support_ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        resolution_notes = request.data.get('resolution_notes')
        ticket = resolve_support_ticket(pk, resolution_notes)
        serializer = self.get_serializer(ticket)
        return Response(serializer.data)

# ViewSet para Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsCompanyUser]

    def create(self, request, *args, **kwargs):
        customer_success_id = request.data.get('customer_success')
        description = request.data.get('description')
        due_date = request.data.get('due_date')
        
        customer_success = CustomerSuccess.objects.get(id=customer_success_id)
        task = create_task(customer_success, description, due_date)
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = complete_task(pk)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

# ViewSet para CustomerFeedback
class CustomerFeedbackViewSet(viewsets.ModelViewSet):
    queryset = CustomerFeedback.objects.all()
    serializer_class = CustomerFeedbackSerializer
    permission_classes = [IsAuthenticated, IsCompanyUser]

    def create(self, request, *args, **kwargs):
        client = request.data.get('client')
        company = request.data.get('company')
        feedback_text = request.data.get('feedback_text')
        feedback_type = request.data.get('feedback_type')
        
        feedback = create_customer_feedback(client, company, feedback_text, feedback_type)
        serializer = self.get_serializer(feedback)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
