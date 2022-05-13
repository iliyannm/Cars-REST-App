from django.utils import timezone
from rest_framework import generics as api_views, status
from rest_framework.response import Response

from cars_restapi.cars_api.models import CarBrand, CarModel
from cars_restapi.cars_api.serializers import CarBrandSerializer, CarModelSerializer


class CarBrandListView(api_views.ListCreateAPIView):
    queryset = CarBrand.objects.filter(deleted_at=None)
    serializer_class = CarBrandSerializer


class SingleCarBrandView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.filter(deleted_at=None)
    serializer_class = CarBrandSerializer

    def destroy(self, request, *args, **kwargs):
        car_brand = self.get_object()
        car_brand.deleted_at = timezone.now()
        car_brand.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarModelListView(api_views.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.filter(deleted_at=None)
    serializer_class = CarModelSerializer

    def destroy(self, request, *args, **kwargs):
        car_model = self.get_object()
        car_model.deleted_at = timezone.now()
        car_model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
