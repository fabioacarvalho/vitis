from django.db import models
from core.models import Company
from login.models import CompanyUser


class Lead(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(CompanyUser, on_delete=models.SET_NULL, null=True, blank=True)  # Vendedor ou responsável pelo lead
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    status_choices = [
        ('new', 'Novo'),
        ('contacted', 'Contato Realizado'),
        ('qualified', 'Qualificado'),
        ('unqualified', 'Desqualificado'),
        ('converted', 'Convertido em Oportunidade'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.status}"

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'


class Deal(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="deals")  # Referência ao Lead
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    stage_choices = [
        ('prospecting', 'Prospecção'),
        ('negotiation', 'Negociação'),
        ('closed_won', 'Fechado - Ganhou'),
        ('closed_lost', 'Fechado - Perdeu'),
    ]
    stage = models.CharField(max_length=20, choices=stage_choices, default='prospecting')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    expected_close_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.lead.name} - {self.stage}"

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'


class Stage(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()  # A ordem define onde esse estágio aparece no pipeline
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'
        ordering = ['order']


class Activity(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name="activities")
    activity_type_choices = [
        ('call', 'Chamada'),
        ('meeting', 'Reunião'),
        ('email', 'E-mail'),
        ('task', 'Tarefa'),
    ]
    activity_type = models.CharField(max_length=20, choices=activity_type_choices)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CompanyUser, on_delete=models.SET_NULL, null=True)  # Quem realizou a atividade

    def __str__(self):
        return f"{self.activity_type} - {self.deal.lead.name}"

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
