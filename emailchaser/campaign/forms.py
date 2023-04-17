from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'message', 'leads', 'schedule_time']
        widgets = {
            'schedule_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
