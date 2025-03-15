from django.db import models
from core.models import Company
from clients.models import Client
from sales.models import Lead

"""
Relações e Funcionalidades
	•	CustomerSuccess: Serve como a base para o sucesso do cliente, ligando a empresa e o cliente.
	•	Engagement: Registra as interações com o cliente, para que você possa acompanhar como a empresa está se relacionando com o cliente.
	•	SupportTicket: Permite registrar e acompanhar os tickets de suporte, para que o sucesso do cliente seja medido com base no suporte prestado.
	•	Task: Acompanha as tarefas ou ações que precisam ser feitas com o cliente.
	•	CustomerFeedback: Coleta feedbacks dos clientes sobre os serviços ou produtos.
"""


class CustomerSuccess(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    nps_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Exemplo de métrica
    retention_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Exemplo de métrica
    last_engaged = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Success for {self.client} (Company: {self.company})"


class Engagement(models.Model):
    lead = models.ForeignKey(Lead, null=True, blank=True, on_delete=models.SET_NULL)  # Relacionando com Lead
    customer_success = models.ForeignKey(CustomerSuccess, on_delete=models.CASCADE, related_name='engagements')
    date = models.DateTimeField(auto_now_add=True)
    interaction_type = models.CharField(max_length=100)  # Exemplo: 'Call', 'Email', etc.
    notes = models.TextField()

    def __str__(self):
        return f"Engagement with {self.customer_success.client} on {self.date}"


class SupportTicket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    issue_description = models.TextField()
    resolution_notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Ticket for {self.client} (Company: {self.company})"


class Task(models.Model):
    customer_success = models.ForeignKey(CustomerSuccess, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Task for {self.customer_success.client} - {self.description}"


class CustomerFeedback(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback_text = models.TextField()
    feedback_type = models.CharField(max_length=100)  # Exemplo: 'Positive', 'Negative', etc.

    def __str__(self):
        return f"Feedback from {self.client} on {self.feedback_date}"
