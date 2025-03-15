# marketing/serializers.py
from rest_framework import serializers
from .models import Campaign, LeadCampaign
from .services import MarketingService

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Criação de uma nova campanha.
        """
        campaign = MarketingService.create_campaign(validated_data)
        return campaign
    
    def assign_lead_to_campaign(self, lead_id):
        """
        Atribui um lead à campanha.
        """
        lead = LeadCampaign.objects.get(id=lead_id)
        campaign = self.instance  # A campanha associada ao objeto de campanha em questão
        return MarketingService.assign_lead_to_campaign(lead, campaign)
    
    def send_bulk_emails(self):
        """
        Envia e-mails para todos os leads associados a esta campanha.
        """
        campaign = self.instance
        MarketingService.send_bulk_campaign_emails(campaign)
