from django.core.exceptions import RegexValidator


class CardNumberValidator(RegexValidator):
    regex = '^[XTW0-9](8,15)$'
    message = '''Card Number must contain only digitials
                or XTW and have length be from 8 to 16 chars'''
    code = 'invalid_card_number'
