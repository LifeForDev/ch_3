from django.test import TestCase
from django.test import Client

from .models import Lead


class SlugTestCase(TestCase):
    def setUp(self):
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="Petr")
        Lead.objects.create(name="create")
        Lead.objects.create(name="delete")

    def test_create_slug_unique(self):
        leads_length = Lead.objects.all().count()
        self.assertEqual(leads_length, 6)

    def test_create_slug_permission(self):
        result = Lead.objects.filter(slug__in=['create', 'delete'])
        self.assertFalse(result)
