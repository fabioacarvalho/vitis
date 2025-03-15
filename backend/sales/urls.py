from django.urls import path
from .views import LeadListView, LeadCreateView, LeadUpdateView, LeadDeleteView, DealListView, DealCreateView, DealUpdateView, DealDeleteView, StageListView, StageCreateView, StageUpdateView, StageDeleteView, ActivityListView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView

app_name = "sales"

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/create/', LeadCreateView.as_view(), name='lead-create'),
    path('leads/<int:lead_id>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:lead_id>/delete/', LeadDeleteView.as_view(), name='lead-delete'),

    path('deals/', DealListView.as_view(), name='deal-list'),
    path('deals/create/', DealCreateView.as_view(), name='deal-create'),
    path('deals/<int:deal_id>/update/', DealUpdateView.as_view(), name='deal-update'),
    path('deals/<int:deal_id>/delete/', DealDeleteView.as_view(), name='deal-delete'),

    path('stages/', StageListView.as_view(), name='stage-list'),
    path('stages/create/', StageCreateView.as_view(), name='stage-create'),
    path('stages/<int:stage_id>/update/', StageUpdateView.as_view(), name='stage-update'),
    path('stages/<int:stage_id>/delete/', StageDeleteView.as_view(), name='stage-delete'),

    path('activities/', ActivityListView.as_view(), name='activity-list'),
    path('activities/create/', ActivityCreateView.as_view(), name='activity-create'),
    path('activities/<int:activity_id>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('activities/<int:activity_id>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
]
