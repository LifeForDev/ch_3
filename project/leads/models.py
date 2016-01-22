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
            max_length=6, choices=GENDER_CHOICES, default='Male')
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    professional = models.CharField(
            max_length=3, choices=PROFESSIONAL_CHOICES, default='No')
    slug = models.SlugField(max_length=40, unique=True)


class Language(models.Model):
    name = models.CharField(max_length=120)
    lead = models.ForeignKey(Lead)
