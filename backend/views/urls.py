from views.views import dashboard, changelist, changeform, changeform_edit

from django.urls import path, include, re_path as url

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('<str:app>/<str:model>/', changelist, name="changelist"),
    path('<str:app>/<str:model>/add/', changeform, name="changeform"),
    path('<str:app>/<str:model>/<int:pk>/', changeform_edit, name="changeform-edit"),
]
