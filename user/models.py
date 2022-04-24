from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.validators import mobile_number_validator
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    password = models.CharField(max_length=128, null=True, blank=True)
    mobile_number = models.CharField(max_length=13, unique=True, validators=[mobile_number_validator])

    objects = CustomUserManager()
    USERNAME_FIELD = "mobile_number"

    def __str__(self):
        return f"{self.mobile_number}"

    def __repr__(self):
        return self.__str__()
