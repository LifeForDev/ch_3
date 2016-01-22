from django import forms

from .models import Lead, Language


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('__all__')
        widgets = {
            'name': forms.InputField()
        }
