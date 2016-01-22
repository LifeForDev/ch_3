from django.shortcuts import render
from django.views.generic import CreateView

from .forms import LeadForm
from .models import Lead


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/form.html'
