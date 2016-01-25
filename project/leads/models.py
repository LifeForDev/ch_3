from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from .validators import ExpiryDateValidator


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
    card_number = models.CharField(
            max_length=16, blank=True,
            validators=[
                RegexValidator(
                    regex=r'^[XTW0-9]{8,15}$',
                    message=_('''Card Number must be contain digital or X T W'
                     and have length from 8 to 15 characters'''),
                    code=_('Invalid_card_number')
                )
            ])
    expiry_date = models.DateField(
            auto_now=False, auto_now_add=False, blank=True,
            null=True, validators=[ExpiryDateValidator])
    professional = models.CharField(
            max_length=3, choices=PROFESSIONAL_CHOICES, default='N')
    slug = models.SlugField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('leads:detail', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Lead.objects.filter(slug=slug).order_by('-pk')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().pk)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Lead)


class Language(models.Model):
    name = models.CharField(max_length=120)
    lead = models.ForeignKey(Lead)

    def __unicode__(self):
        return self.name
