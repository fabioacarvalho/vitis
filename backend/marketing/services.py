# marketing/services.py
from .models import Campaign
from django.core.exceptions import ObjectDoesNotExist

class MarketingService:
    
    @staticmethod
    def create_campaign(data):
        """
        Cria uma nova campanha de marketing.
        """
        campaign = Campaign.objects.create(
            name=data['name'],
            description=data['description'],
            start_date=data['start_date'],
            end_date=data['end_date'],
        )
        return campaign

    @staticmethod
    def update_campaign(campaign_id, data):
        """
        Atualiza uma campanha existente.
        """
        try:
            campaign = Campaign.objects.get(id=campaign_id)
            campaign.name = data.get('name', campaign.name)
            campaign.description = data.get('description', campaign.description)
            campaign.start_date = data.get('start_date', campaign.start_date)
            campaign.end_date = data.get('end_date', campaign.end_date)
            campaign.save()
            return campaign
        except Campaign.DoesNotExist:
            return None

    @staticmethod
    def delete_campaign(campaign_id):
        """
        Deleta uma campanha existente.
        """
        try:
            campaign = Campaign.objects.get(id=campaign_id)
            campaign.delete()
            return True
        except Campaign.DoesNotExist:
            return False
