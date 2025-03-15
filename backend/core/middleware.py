from datetime import datetime
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from core.models import AuditLog


# Save every step into system
# Must be imported into middlewares in settings.py # 'core.middleware.AuditLogMiddleware',
# class AuditLogMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         # Aqui você pode adicionar verificações para auditar ações
#         if request.user.is_authenticated:
#             AuditLog.objects.create(
#                 entity_type='Request',
#                 entity_id=request.user.id,
#                 action='Accessed',
#                 timestamp=now(),
#                 user=request.user
#             )
#         return response
