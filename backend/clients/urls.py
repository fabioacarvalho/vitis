from django.urls import path
from clients.views import ClientCreateView, ClientUpdateView, ClientListView, ClientDeleteView


app_name = "clients"


urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('<int:client_id>/', ClientListView.as_view(), name='client-list'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('update/<int:client_id>/', ClientUpdateView.as_view(), name='client-update'),
    path('delete/<int:client_id>/', ClientDeleteView.as_view(), name='client-delete'),
]