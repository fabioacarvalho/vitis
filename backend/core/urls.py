from django.urls import path
from core.views import CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView


app_name = 'core'


urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/update/<int:company_id>/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/delete/<int:company_id>/', CompanyDeleteView.as_view(), name='company-delete'),
]