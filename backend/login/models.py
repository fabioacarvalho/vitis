from django.db import models
from django.contrib.auth.models import AbstractUser
# from core.models import Company


class CompanyUser(AbstractUser):
    ROLE_CHOICES = (
        ('super', 'Super usuário'),
        ('admin', 'Administrador da Empresa'),
        ('auditor', 'Auditor'),
        ('user', 'Usuário Padrão'),
        ('sales', 'Usuário Vendas'),
        ('marketing', 'Usuário Marketing'),
        ('success', 'Usuário Sucesso do Cliente'),
        ('rh', 'Recursos Humanos'),
        ('manager', 'Gestor'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    company = models.ForeignKey(
        'core.Company',  # Use a referência direta ao invés de string
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='users'
    )
    is_company_admin = models.BooleanField(default=False)
    document = models.CharField(max_length=20, null=True, blank=True)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)


class CompanyInvitation(models.Model):
    company = models.ForeignKey('core.Company', on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('company', 'email')
