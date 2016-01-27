from django.test import TestCase
from django.test import Client

from .models import Lead


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
