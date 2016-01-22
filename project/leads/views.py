from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from .forms import LeadForm
from .models import Lead


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/form.html'
    success_url = reverse_lazy('leads:list')

    def save(self, *args, **kwargs):
        messages.success(_('Successfully created!'))
        super(LeadCreateView, self).save(*args, **kwargs)


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/detail.html'


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'leads/form.html'
    form_class = LeadForm
    success_url = reverse_lazy('leads:list')
    success_message = _('Successfully updated!')


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/list.html'
    paginate_by = 3
