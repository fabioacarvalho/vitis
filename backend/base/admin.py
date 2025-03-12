from django.contrib import admin
from base.models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["father", "admin", "support", "name", "url", "active",]
    list_filter = ["father", "admin", "support", "name", "url", "active",]
    search_fields  = ["father", "admin", "support", "name", "url", "active",]