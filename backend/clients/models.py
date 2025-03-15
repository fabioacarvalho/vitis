from django.db import models
from core.models import Company


class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    cnpj_cpf = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Pode ser CNPJ ou CPF
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["name"]
