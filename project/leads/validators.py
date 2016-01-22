import datetime

from django.core.exceptions import RegexValidator, ValidationError
from django.utils.translation import ugettext_lazy as _


class CardNumberValidator(RegexValidator):
    regex = r'^[XTW0-9]{8,15}$'
    message = _('''Card Number must contain only digitials
        or XTW and have length be from 8 to 16 chars''')
    code = _('invalid_card_number')


def ExpiryDateValidator(value):
    if value < datetime.date.today() + datetime.timedelta(days=365.25/2):
        raise ValidationError(_('Choice a valid date'))
