# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .models import Lead, Deal, Activity, Stage, AuditLog


# """
# 1. Enviando E-mail de Boas-Vindas para um Lead Criado
# Sempre que um novo lead for criado, você pode querer enviar um e-mail de boas-vindas para ele.
# """
# @receiver(post_save, sender=Lead)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         subject = f'Welcome, {instance.name}!'
#         message = f'Hello {instance.name},\n\nThanks for showing interest in our services!'
#         send_mail(subject, message, 'from@example.com', [instance.email])


# """
# 2. Registrar Atividade Sempre que um Deal for Criado ou Atualizado
# Quando um novo deal for criado ou atualizado, você pode registrar automaticamente uma atividade para acompanhar essa mudança. Isso ajuda a manter um histórico de ações no sistema.
# """
# @receiver(post_save, sender=Deal)
# def log_deal_activity(sender, instance, created, **kwargs):
#     if created:
#         activity_type = 'Deal Created'
#         description = f'New deal created for lead: {instance.lead.name}'
#     else:
#         activity_type = 'Deal Updated'
#         description = f'Deal updated for lead: {instance.lead.name}'

#     Activity.objects.create(
#         activity_type=activity_type,
#         description=description,
#         deal=instance,
#         user=instance.lead.user,  # Ou o usuário responsável
#     )


# """
# 3. Atualizar o Status de um Deal Quando Ele Avançar para um Novo Estágio
# Quando um deal é movido para um novo estágio, você pode querer atualizar o seu status automaticamente ou gerar uma atividade.
# """
# @receiver(post_save, sender=Deal)
# def update_deal_status(sender, instance, created, **kwargs):
#     if not created and instance.stage != instance.__class__.objects.get(pk=instance.pk).stage:
#         # Quando o estágio do deal é alterado
#         new_stage = instance.stage
#         activity_type = 'Deal Stage Updated'
#         description = f'Deal moved to stage: {new_stage.name}'

#         Activity.objects.create(
#             activity_type=activity_type,
#             description=description,
#             deal=instance,
#             user=instance.lead.user,  # Ou o usuário responsável
#         )


# """
# 4. Calcular o Valor Total de Todos os Deals de um Lead
# Após a criação ou atualização de um deal, você pode querer recalcular o valor total de todos os deals de um lead. Isso poderia ser feito em uma sinalização.
# """
# @receiver(post_save, sender=Deal)
# def recalculate_lead_total_value(sender, instance, created, **kwargs):
#     lead = instance.lead
#     total_value = lead.deals.aggregate(total_value=models.Sum('value'))['total_value']
#     lead.total_value = total_value
#     lead.save()


# """
# 5. Enviar Notificação para Equipe de Vendas Quando um Deal é Concluído
# Você pode querer notificar sua equipe de vendas quando um deal for concluído ou se algum outro critério for atendido.
# """
# @receiver(post_save, sender=Deal)
# def send_deal_completion_notification(sender, instance, created, **kwargs):
#     if instance.status == 'Completed':  # Ajuste conforme a lógica de status do seu sistema
#         subject = 'Deal Completed'
#         message = f'A deal with lead {instance.lead.name} has been completed successfully.'
#         send_mail(subject, message, 'sales-team@example.com', ['sales-manager@example.com'])


# """
# 6. Registrar Auditoria de Mudanças de Estágio ou Status
# Para garantir que todas as alterações no sistema sejam auditadas, você pode registrar a mudança de status de um deal.
# """
# @receiver(post_save, sender=Deal)
# def log_deal_status_change(sender, instance, created, **kwargs):
#     if not created:
#         previous_status = instance.__class__.objects.get(pk=instance.pk).status
#         if previous_status != instance.status:
#             AuditLog.objects.create(
#                 entity_type='Deal',
#                 entity_id=instance.id,
#                 action='Status Changed',
#                 previous_value=previous_status,
#                 new_value=instance.status,
#             )


# """
# 7. Atualizar o Status de um Lead Quando Ele For Movido para um Novo Estágio
# Caso um lead passe por um processo de qualificação, você pode querer atualizar o status do lead.
# """
# @receiver(post_save, sender=Deal)
# def update_lead_status(sender, instance, created, **kwargs):
#     if created:
#         lead = instance.lead
#         if instance.stage.name == 'Closed Won':
#             lead.status = 'Qualified'
#             lead.save()

