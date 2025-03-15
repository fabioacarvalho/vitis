from django.db import models
from login.models import CompanyUser


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    cnpj = models.CharField(max_length=14, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    code = models.CharField(max_length=25, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    logo = models.ImageField(upload_to='company', null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
        ('Deleted', 'Deleted'),
        ('Status Changed', 'Status Changed'),
        ('Assigned', 'Assigned'),
        # Adicione mais ações conforme necessário
    ]
    
    entity_type = models.CharField(max_length=255)
    entity_id = models.PositiveIntegerField()
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    previous_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CompanyUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.entity_type} {self.entity_id} - {self.action}'

    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
        ordering = ['-timestamp']
