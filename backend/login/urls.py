from django.urls import path
from login.views import UserListView

app_name = "users"


urlpatterns = [
    path('', UserListView.as_view(), name='client-list'),
    path('<int:user_id>/', UserListView.as_view(), name='client-list'),
]