# urls.py

from django.urls import path
from .views import lead_list, LeadCreateView, LeadUpdateView, LeadDeleteView, lead_detail

urlpatterns = [
    path("", lead_list, name="lead_list"),
    path("<int:pk>/", lead_detail, name="lead_detail"),
    path("create/", LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/update/", LeadUpdateView.as_view(), name="lead_update"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="lead_delete"),
]
