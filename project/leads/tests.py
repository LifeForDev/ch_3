import datetime

from django.test import TestCase

from .models import Lead
from .forms import LeadForm


class SlugTestCase(TestCase):

    def setUp(self):
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="create")
        Lead.objects.create(name="delete")

    def test_create_slug_unique(self):
        leads_petr = Lead.objects.filter(name='Petr')
        first_petr_slug = leads_petr[0].slug
        second_petr_slug = leads_petr[1].slug
        self.assertNotEqual(first_petr_slug, second_petr_slug)

    def test_create_slug_permission(self):
        result = Lead.objects.filter(slug__in=['create', 'delete'])
        self.assertFalse(result)


class LeadFormTestCase(TestCase):

    lead_Petr = {
        'name': 'Petr',
        'gender': 'M',
        'professional': 'Y',
    }

    def test_card_number(self):
        self.lead_Petr['expiry_date'] = '3000-01-01'

        incorrect_number = [
            'XXXX',  # too short
            'XXXXXXXXXXXXXXXXXXXXXXX',  # too long
            'XXXXXXXXXXXXZZZZZ',  # prohibit char
            '12321321312xxxxx',  # lower-case char
            '',  # empty card number, when expiry date
        ]

        for number in incorrect_number:
            self.lead_Petr['card_number'] = number
            self.assertFalse(LeadForm(self.lead_Petr).is_valid())

    def test_expiry_date(self):
        self.lead_Petr['card_number'] = '1234567890'

        date_more_6_month = datetime.date.today() \
            + datetime.timedelta(days=365.25 / 2)
        self.lead_Petr['expiry_date'] = date_more_6_month

        self.assertTrue(LeadForm(self.lead_Petr).is_valid())

        incorrect_date = [
            datetime.date.today(),  # date today
            datetime.date.today() - datetime.timedelta(days=3),  # past date
            ''  # empty date when card number
        ]

        for date in incorrect_date:
            self.lead_Petr['expiry_date'] = date
            self.assertFalse(LeadForm(self.lead_Petr).is_valid())
