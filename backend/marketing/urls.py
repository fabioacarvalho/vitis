# marketing/urls.py
from django.urls import path
from .views import CampaignListView, CampaignCreateView, CampaignUpdateView, CampaignDeleteView

app_name = "marketing"

urlpatterns = [
    path('campaigns/', CampaignListView.as_view(), name='campaign-list'),
    path('campaigns/create/', CampaignCreateView.as_view(), name='campaign-create'),
    path('campaigns/<int:campaign_id>/update/', CampaignUpdateView.as_view(), name='campaign-update'),
    path('campaigns/<int:campaign_id>/delete/', CampaignDeleteView.as_view(), name='campaign-delete'),
]
