from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.utils.timezone import now
from login.models import CompanyUser
from .models import AuditLog


@receiver(post_save)
def log_entity_creation(sender, instance, created, **kwargs):
    # Evitar recursão infinita (não logar se o modelo for AuditLog)
    if sender == AuditLog:
        return

    if created:
        AuditLog.objects.create(
            entity_type=sender.__name__,
            entity_id=instance.pk,
            action='Created',
            timestamp=now(),
            user=instance.created_by if hasattr(instance, 'created_by') else None  # Ajuste conforme necessário
        )

@receiver(pre_save)
def log_entity_update(sender, instance, **kwargs):
    if not instance.pk:  # Não logar se for uma criação, pois isso será tratado pelo post_save
        return
    
    # Compare os valores anteriores e novos para registrar a alteração
    previous = sender.objects.get(pk=instance.pk)
    for field in instance._meta.fields:
        field_name = field.name
        if getattr(previous, field_name) != getattr(instance, field_name):
            AuditLog.objects.create(
                entity_type=sender.__name__,
                entity_id=instance.pk,
                action='Updated',
                previous_value=str(getattr(previous, field_name)),
                new_value=str(getattr(instance, field_name)),
                timestamp=now(),
                user=instance.modified_by if hasattr(instance, 'modified_by') else None  # Ajuste conforme necessário
            )

@receiver(pre_delete)
def log_entity_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        entity_type=sender.__name__,
        entity_id=instance.pk,
        action='Deleted',
        timestamp=now(),
        user=instance.modified_by if hasattr(instance, 'modified_by') else None  # Ajuste conforme necessário
    )
