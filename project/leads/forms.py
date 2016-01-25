from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

from bootstrap3_datetime.widgets import DateTimePicker

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import InlineRadios, FieldWithButtons, StrictButton

from .models import Lead, Language


class LeadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        # self.helper = FormHelper(self)
        # self.helper.form_method = 'POST'
        # self.helper.form_action = '#'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-sm-2'
        # self.helper.field_class = 'col-sm-10'
        # self.helper.add_input(Submit('submit', _('Submit'),
        #                              css_class='btn btn-default'))
        # self.helper.layout = Layout(
        #     Field('name', placeholder=_('John Doe')),
        #     InlineRadios('gender'),
        #     Field('card_number', placeholder=_('XXXXXXXXXXXXXXXX')),
        #     Field('expiry_date', placeholder=_('2015-11-20')),
        #     InlineRadios('professional'),
        #     Field('slug')
        # )

        self.helper1 = FormHelper(self)
        self.helper1.form_tag = False
        # print dir(self.helper1)
        print dir(self.helper1['name'].update_attributes)
        # self.helper1['name'].wrap(Field, wrapper_class="housenumber")
        self.helper1.label_class = 'col-sm-2'
        self.helper1.field_class = 'col-sm-10'
        self.helper1.layout = Layout(
            Field('name', placeholder=_('John Doe'), wrapper_class="row"),
            InlineRadios('gender', wrapper_class="row")
        )

        self.helper2 = FormHelper(self)
        self.helper2.form_tag = False
        self.helper2.disable_csrf = True
        self.helper2.label_class = 'col-sm-2'
        self.helper2.field_class = 'col-sm-10'
        self.helper2.layout = Layout(
            Field('card_number', placeholder=_('XXXXXXXXXXXXXXXX'),
                  wrapper_class="row"),
            Field('expiry_date', placeholder=_('2015-11-20'),
                  wrapper_class="row"),
            InlineRadios('professional', wrapper_class="row"),
        )

    class Meta:
        model = Lead
        exclude = ['slug']
        widgets = {
            'gender': RadioSelect(),
            'expiry_date': DateTimePicker(options={'format': 'YYYY-MM-DD'}),
            'professional': RadioSelect(),
        }


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'language_form row'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.fields['name'].label = _('Language')
        self.helper.layout = Layout(
            FieldWithButtons(
                Field('name', placeholder=_('English')),
                StrictButton("Add", onclick="addField(event)")),
            )

    class Meta:
        model = Language
        fields = ('name',)


LanguageFormset = inlineformset_factory(
    Lead,
    Language,
    form=LanguageForm,
    extra=1,
    can_delete=False
)
