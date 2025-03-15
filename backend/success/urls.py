from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomerSuccessViewSet, EngagementViewSet, SupportTicketViewSet, TaskViewSet, CustomerFeedbackViewSet

app_name = "success"

router = DefaultRouter()
router.register(r'customer-success', CustomerSuccessViewSet)
router.register(r'engagements', EngagementViewSet)
router.register(r'support-tickets', SupportTicketViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'customer-feedbacks', CustomerFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]