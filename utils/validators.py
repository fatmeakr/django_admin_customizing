from django.core.validators import RegexValidator

mobile_number_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message="Mobile number format is incorrect",
)