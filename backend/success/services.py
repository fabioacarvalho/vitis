from datetime import timezone
from .models import CustomerSuccess, Engagement, SupportTicket, Task, CustomerFeedback
from django.db import transaction

# Serviço para criar um novo CustomerSuccess
def create_customer_success(client, company, nps_score=None, retention_rate=None):
    customer_success = CustomerSuccess.objects.create(
        client=client,
        company=company,
        nps_score=nps_score,
        retention_rate=retention_rate
    )
    return customer_success

# Serviço para registrar um novo Engagement
def create_engagement(customer_success, interaction_type, notes, lead=None,):
    engagement = Engagement.objects.create(
        lead=lead,
        customer_success=customer_success,
        interaction_type=interaction_type,
        notes=notes
    )
    return engagement

# Serviço para criar um SupportTicket
def create_support_ticket(client, company, issue_description, resolution_notes=None):
    support_ticket = SupportTicket.objects.create(
        client=client,
        company=company,
        issue_description=issue_description,
        resolution_notes=resolution_notes
    )
    return support_ticket

# Serviço para criar uma Task
def create_task(customer_success, description, due_date):
    task = Task.objects.create(
        customer_success=customer_success,
        description=description,
        due_date=due_date
    )
    return task

# Serviço para registrar CustomerFeedback
def create_customer_feedback(client, company, feedback_text, feedback_type):
    feedback = CustomerFeedback.objects.create(
        client=client,
        company=company,
        feedback_text=feedback_text,
        feedback_type=feedback_type
    )
    return feedback

# Serviço para resolver um SupportTicket
def resolve_support_ticket(ticket_id, resolution_notes):
    ticket = SupportTicket.objects.get(id=ticket_id)
    ticket.resolved_at = timezone.now()
    ticket.resolution_notes = resolution_notes
    ticket.save()
    return ticket

# Serviço para marcar Task como completada
def complete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return task
