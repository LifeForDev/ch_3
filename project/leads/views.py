from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
    CreateView, DetailView, ListView,
    UpdateView, RedirectView
)
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect

from .forms import LeadForm, LanguageFormset
from .models import Lead


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LeadCreateView, self).get_context_data(*args, **kwargs)
        context['formset'] = LanguageFormset(self.request.POST or None)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, _('Lead successfully created!'))
            return redirect(reverse('leads:list'))
        else:
            messages.error(self.request, _('Pls fill the languages'))
            return self.form_invalid(form)


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/detail.html'


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'leads/form.html'
    form_class = LeadForm
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, *args, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(*args, **kwargs)
        context['formset'] = LanguageFormset(self.request.POST or None, instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, _('Lead successfully updated!'))
            return redirect(reverse('leads:list'))
        else:
            messages.error(self.request, _('Pls fill the languages'))
            return self.form_invalid(form)


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/list.html'
    paginate_by = 10


class LeadDeleteView(RedirectView):
    url = reverse_lazy('leads:list')

    def post(self, request, *args, **kwargs):
        delete_leads = request.POST.get('ids').split(',')
        if delete_leads:
            queryset = Lead.objects.filter(id__in=delete_leads)
            queryset.delete()
            messages.success(self.request, _('Successfully deleted!'))
        return super(LeadDeleteView, self).post(request, *args, **kwargs)
