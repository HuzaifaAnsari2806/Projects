from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError


def validate_unit_of_measurements(value):
    ureg=pint.UnitRegistry()
    try:
        single_unit=ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} not a valid unit")
    # if value not in valid_unit_of_measurements:
    #     raise ValidationError(f"{value} not a valid unit")