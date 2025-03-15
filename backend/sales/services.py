from .models import Lead, Deal, Stage, Activity
from django.db import transaction
from django.core.exceptions import ValidationError

class LeadService:
    @staticmethod
    def create_lead(data):
        try:
            lead = Lead.objects.create(
                company=data['company'],
                user=data.get('user', None),  # Pode ser None caso não tenha um vendedor atribuído
                name=data['name'],
                email=data['email'],
                phone=data.get('phone', ''),
                status='new',  # Status inicial como "Novo"
                notes=data.get('notes', ''),
            )
            return lead
        except Exception as e:
            raise ValidationError(f"Error creating lead: {str(e)}")
    
    @staticmethod
    def get_leads_by_company(company):
        return Lead.objects.filter(company=company)

    @staticmethod
    def get_lead_by_id(lead_id):
        return Lead.objects.get(id=lead_id)

class DealService:
    @staticmethod
    def create_deal(data):
        try:
            lead = Lead.objects.get(id=data['lead_id'])
            deal = Deal.objects.create(
                lead=lead,
                company=lead.company,
                stage=data.get('stage', 'prospecting'),
                value=data['value'],
                expected_close_date=data.get('expected_close_date', None),
                notes=data.get('notes', ''),
            )
            return deal
        except Lead.DoesNotExist:
            raise ValidationError("Lead does not exist.")
        except Exception as e:
            raise ValidationError(f"Error creating deal: {str(e)}")

    @staticmethod
    def update_deal(deal_id, data):
        try:
            deal = Deal.objects.get(id=deal_id)
            deal.stage = data.get('stage', deal.stage)
            deal.value = data.get('value', deal.value)
            deal.expected_close_date = data.get('expected_close_date', deal.expected_close_date)
            deal.notes = data.get('notes', deal.notes)
            deal.save()
            return deal
        except Deal.DoesNotExist:
            raise ValidationError("Deal does not exist.")
        except Exception as e:
            raise ValidationError(f"Error updating deal: {str(e)}")
    
    @staticmethod
    def get_deals_by_company(company):
        return Deal.objects.filter(company=company)

    @staticmethod
    def get_deal_by_id(deal_id):
        return Deal.objects.get(id=deal_id)

    @staticmethod
    def move_deal_to_next_stage(deal):
        stages = Stage.objects.filter(company=deal.company).order_by('order')
        current_stage_index = list(stages).index(deal.stage)
        if current_stage_index + 1 < len(stages):
            deal.stage = stages[current_stage_index + 1].name
            deal.save()
            return deal
        raise ValidationError("This deal cannot be moved to the next stage.")

class StageService:
    @staticmethod
    def create_stage(data):
        try:
            stage = Stage.objects.create(
                name=data['name'],
                order=data['order'],
                company=data['company'],
            )
            return stage
        except Exception as e:
            raise ValidationError(f"Error creating stage: {str(e)}")

    @staticmethod
    def get_stages_by_company(company):
        return Stage.objects.filter(company=company)

    @staticmethod
    def get_stage_by_id(stage_id):
        return Stage.objects.get(id=stage_id)

class ActivityService:
    @staticmethod
    def create_activity(data):
        try:
            deal = Deal.objects.get(id=data['deal_id'])
            activity = Activity.objects.create(
                deal=deal,
                activity_type=data['activity_type'],
                description=data['description'],
                user=data.get('user', None),  # O usuário que fez a atividade
            )
            return activity
        except Deal.DoesNotExist:
            raise ValidationError("Deal does not exist.")
        except Exception as e:
            raise ValidationError(f"Error creating activity: {str(e)}")

    @staticmethod
    def get_activities_by_deal(deal):
        return Activity.objects.filter(deal=deal)
