from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

UserModel = get_user_model()

NAME_MAX_LENGTH = 20


class CarBrand(models.Model):

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        default=None
    )


class CarModel(models.Model):

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        default=None
    )


class UserCar(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )

    first_reg = models.DateTimeField(
        blank=True,
        null=True,
    )

    odometer = models.IntegerField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        default=None
    )

