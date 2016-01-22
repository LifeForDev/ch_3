from django import forms
from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

from bootstrap3_datetime.widgets import DateTimePicker

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from crispy_forms.bootstrap import InlineRadios

from .models import Lead


class LeadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', _('Submit'),
                                     css_class='btn btn-default'))
        self.helper.layout = Layout(
            Field('name', placeholder=_('John Doe')),
            InlineRadios('gender'),
            Field('card_number', placeholder=_('XXXXXXXXXXXXXXXX')),
            Field('expiry_date', placeholder=_('2015-11-20')),
            InlineRadios('professional'),
            Field('slug')
        )

    class Meta:
        model = Lead
        exclude = ['slug']
        # fields = '__all__'
        widgets = {
            'gender': RadioSelect(),
            'expiry_date': DateTimePicker(options={'format': 'YYYY-MM-DD'}),
            'professional': RadioSelect(),
        }
