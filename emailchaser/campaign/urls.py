from django.urls import path
from .views import campaign_list, CampaignCreateView, CampaignEditView, CampaignDeleteView, CampaignDetailView
urlpatterns = [
    path("", campaign_list, name="campaign_list"),
    path("create/", CampaignCreateView.as_view(), name="campaign_create"),
    path("<int:id>/update/", CampaignEditView.as_view(), name="campaign_edit"),
    path("<int:id>/delete/", CampaignDeleteView.as_view(), name="campaign_delete"),
    path("<int:id>/detail/", CampaignDetailView.as_view(), name="campaign_detail"),
]
