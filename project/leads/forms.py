from django import forms
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory
from django.forms.widgets import RadioSelect, HiddenInput
from django.forms.formsets import DELETION_FIELD_NAME
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import InlineRadios, FieldWithButtons, StrictButton

from .models import Lead, Language


class LeadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        self.helper1 = FormHelper(self)
        self.helper1.form_tag = False
        self.helper1.form_show_errors = True
        self.helper1.label_class = 'col-sm-2'
        self.helper1.field_class = 'col-sm-10'
        self.helper1.layout = Layout(
            Field('name', placeholder=_('John Doe'), wrapper_class="row"),
            InlineRadios('gender', wrapper_class="row")
        )

        self.helper2 = FormHelper(self)
        self.helper2.form_show_errors = True
        self.helper2.form_tag = False
        self.helper2.disable_csrf = True
        self.helper2.label_class = 'col-sm-2'
        self.helper2.field_class = 'col-sm-10'
        self.helper2.layout = Layout(
            Field('card_number', placeholder=_('XXXXXXXXXXXXXXXX'),
                  wrapper_class="row"),
            Field('expiry_date', placeholder=_('2015-11-20'),
                  wrapper_class="row", css_class="datepicker", id="datepicker"),
            InlineRadios('professional', wrapper_class="row"),
        )

    class Meta:
        model = Lead
        exclude = ['slug']
        widgets = {
            'gender': RadioSelect(),
            'professional': RadioSelect(),
        }


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'language_form row'
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.disable_csrf = True
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.fields['name'].label = _('Language')
        self.helper.layout = Layout(
            FieldWithButtons(
                Field('name', placeholder=_('English')),
                StrictButton("Add")),
            )

    class Meta:
        model = Language
        fields = ('name',)


class RequiredFirstFormSet(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        if count < 1:
            raise forms.ValidationError(_('You must have at least one Language'))

    def add_fields(self, form, index):
        # Hide delete checkbox from formset
        super(RequiredFirstFormSet, self).add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].widget = HiddenInput()


LanguageFormset = inlineformset_factory(
    Lead,
    Language,
    form=LanguageForm,
    formset=RequiredFirstFormSet,
    extra=1,
    can_delete=True
)
