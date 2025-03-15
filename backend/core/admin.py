from django.contrib import admin
from .models import Company, AuditLog


admin.site.register(Company)
# admin.site.register(AuditLog)


class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('entity_type', 'entity_id', 'action', 'timestamp', 'user')  # Campos a serem exibidos
    list_filter = ('action', 'entity_type', 'timestamp', 'user')  # Filtros para a barra lateral
    search_fields = ('entity_type', 'entity_id', 'action', 'user__username')  # Campos pesquisáveis
    ordering = ('-timestamp',)  # Ordena por timestamp em ordem decrescente
    readonly_fields = ('entity_type', 'entity_id', 'action', 'previous_value', 'new_value', 'timestamp', 'user')  # Campos somente leitura
    date_hierarchy = 'timestamp'  # Permite filtrar por data

# Registrar o modelo e o admin
admin.site.register(AuditLog, AuditLogAdmin)
