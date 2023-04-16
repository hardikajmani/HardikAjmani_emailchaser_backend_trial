# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lead
from .forms import LeadForm

class LeadCreateView(CreateView):
    model = Lead
    fields = ["user_name", "email_address", "company", "website", "registered_user"]
    template_name = "lead_form.html"
    success_url = reverse_lazy("lead_list")


class LeadUpdateView(UpdateView):
    model = Lead
    fields = ["user_name", "email_address", "company", "website", "registered_user"]
    template_name = "lead_form.html"
    success_url = reverse_lazy("lead_list")


class LeadDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy("lead_list")
    template_name = "lead_confirm_delete.html"


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "lead_main.html", {"leads": leads})

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, "lead_detail.html", {"lead": lead})

def lead_create(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.registered_user = request.user
            lead.save()
            return redirect("lead_list")
    else:
        form = LeadForm()
    return render(request, "lead_form.html", {"form": form})

def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()
            return redirect("lead_list")
    else:
        form = LeadForm(instance=lead)
    return render(request, "lead_form.html", {"form": form})