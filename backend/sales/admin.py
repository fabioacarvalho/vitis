from django.contrib import admin
from sales.models import Lead, Deal, Stage, Activity


admin.site.register(Lead)
admin.site.register(Deal)
admin.site.register(Stage)
admin.site.register(Activity)
