from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from .forms import LeadForm, LanguageFormset
from .models import Lead


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/form.html'
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, *args, **kwargs):
        context = super(LeadCreateView, self).get_context_data(*args, **kwargs)
        context['formset'] = LanguageFormset(self.request.POST or None)
        return context

    def form_valid(self, form):
        # context = self.get_context_data()
        # formset = context['formset']
        instance = form.save(commit=False)
        formset = LanguageFormset(self.request.POST, instance=instance)
        if formset.is_valid:
            form.save()
            formset.save()
            return super(LeadCreateView, self).form_valid(form)

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

    def get_context_data(self, *args, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(*args, **kwargs)
        context['formset'] = LanguageFormset(self.request.POST or None, instance=self.object)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        formset = LanguageFormset(self.request.POST, instance=instance)
        if formset.is_valid:
            form.save()
            formset.save()
            return super(LeadUpdateView, self).form_valid(form)


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/list.html'
    paginate_by = 10
