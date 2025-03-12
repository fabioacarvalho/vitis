from django.db import models

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
