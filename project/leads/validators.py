import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def ExpiryDateValidator(value):
    if value < datetime.date.today() + datetime.timedelta(days=365.25/2):
        raise ValidationError(_('Choice a valid date'))
