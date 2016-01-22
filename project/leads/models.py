from __future__ import unicode_literals

from django.db import models


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

PROFESSIONAL_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)


class Lead(models.Model):
    name = models.CharField(max_length=120)
    gender = models.CharField(
            max_length=6, choices=GENDER_CHOICES, default='M')
    card_number = models.CharField(max_length=16, blank=True)
    expiry_date = models.DateField(
            auto_now=False, auto_now_add=False, blank=True, null=True)
    professional = models.CharField(
            max_length=3, choices=PROFESSIONAL_CHOICES, default='N')
    slug = models.SlugField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug


class Language(models.Model):
    name = models.CharField(max_length=120)
    lead = models.ForeignKey(Lead)

    def __unicode__(self):
        return self.name
