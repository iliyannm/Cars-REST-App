from django.contrib.auth import models as auth_models
from django.core import validators as auth_validators
from django.db import models

from cars_restapi.accounts.managers import CarsAppUserManager


class CarsAppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    USERNAME_MIN_LENGTH = 5
    USERNAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=(
            auth_validators.MinLengthValidator(USERNAME_MIN_LENGTH),
            auth_validators.MaxLengthValidator(USERNAME_MAX_LENGTH),
        )
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        max_length=max(len(x) for x, y in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    objects = CarsAppUserManager()
