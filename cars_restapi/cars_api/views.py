from rest_framework import generics as api_views
from cars_restapi.cars_api.models import UserCar, CarBrand, CarModel
from cars_restapi.cars_api.serializers import CarBrandSerializer, CarModelSerializer


class CarBrandListView(api_views.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class SingleCarBrandView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelListView(api_views.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

# 1. Login / Register functionality - how to do it
# 2. How to create the UserCar object
# 3. How to fix the SoftDelete thing
