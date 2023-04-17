from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Campaign
from .forms import CampaignForm
from django.urls import reverse_lazy

# Create your views here.
# list of all campaigns
@login_required
def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, "campaign_list.html", {"campaigns": campaigns})

# Add campaign
class CampaignCreateView(LoginRequiredMixin, View):
    template_name = 'campaign_create.html'
    form_class = CampaignForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.registerd_user = request.user # Set the registered user as current user
            campaign.save()
            return redirect('campaign_list')
        

class CampaignEditView(LoginRequiredMixin, View):
    template_name = 'campaign_edit.html'
    form_class = CampaignForm

    def get(self, request, id):
        campaign = get_object_or_404(Campaign, id=id)
        form = self.form_class(instance=campaign)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        campaign = get_object_or_404(Campaign, id=id)
        form = self.form_class(request.POST, instance=campaign)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.registered_user = request.user  # Set the registered user as the current user
            campaign.save()
            form.save_m2m()
            return redirect('campaign_list')
        return render(request, self.template_name, {'form': form})

class CampaignDeleteView(LoginRequiredMixin, DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')
    template_name = 'campaign_delete.html'


class CampaignDetailView(LoginRequiredMixin, DetailView):
    template_name = 'campaign_detail.html'

    def get(self, request, id):
        campaign = get_object_or_404(Campaign, id=id)
        leads = campaign.leads.all()
        return render(request, self.template_name, {'campaign': campaign, "leads": leads})