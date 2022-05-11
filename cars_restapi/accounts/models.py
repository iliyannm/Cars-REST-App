from django.contrib.auth import models as auth_models
from django.core import validators as auth_validators
from django.db import models

from cars_restapi.accounts.managers import CarsAppUserManager


class CarsAppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
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

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'

    objects = CarsAppUserManager()


class Profile(models.Model):
    NAME_MIN_LENGTH = 5
    NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LENGTH,
        validators=(
            auth_validators.MinLengthValidator(NAME_MIN_LENGTH),
            auth_validators.MaxLengthValidator(NAME_MAX_LENGTH),
        )
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
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

    user = models.OneToOneField(
        CarsAppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name
