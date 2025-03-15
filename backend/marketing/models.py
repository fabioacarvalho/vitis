# marketing/models.py
from django.db import models
from sales.models import Lead  # Reutilizando a model Lead de Sales


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class LeadCampaign(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    engagement_status = models.CharField(max_length=20, choices=[('engaged', 'Engaged'), ('not_engaged', 'Not Engaged')], default='not_engaged')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead} - {self.campaign.name}"


