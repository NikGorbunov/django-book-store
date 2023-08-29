from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_integer_price(value):
    if not isinstance(value, int):
        raise ValidationError(
            _('%(value)s is not an integer'),
            params={'value': value},
        )
