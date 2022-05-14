from cars_restapi.cars_api.models import UserCar, CarBrand, CarModel
from rest_framework import serializers


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ('car_model', 'car_brand')
