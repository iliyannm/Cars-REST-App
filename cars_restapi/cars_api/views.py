from django.utils import timezone
from rest_framework import generics as api_views, status, permissions
from rest_framework.response import Response

from cars_restapi.cars_api.models import CarBrand, CarModel, UserCar
from cars_restapi.cars_api.serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


class CarBrandListView(api_views.ListCreateAPIView):
    queryset = CarBrand.objects.filter(deleted_at=None)
    serializer_class = CarBrandSerializer


class SingleCarBrandView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.filter(deleted_at=None)
    serializer_class = CarBrandSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def destroy(self, request, *args, **kwargs):
        car_brand = self.get_object()
        car_brand.deleted_at = timezone.now()
        car_brand.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarModelListView(api_views.ListCreateAPIView):
    queryset = CarModel.objects.filter(deleted_at=None)
    serializer_class = CarModelSerializer


class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.filter(deleted_at=None)
    serializer_class = CarModelSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def destroy(self, request, *args, **kwargs):
        car_model = self.get_object()
        car_model.deleted_at = timezone.now()
        car_model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCarCreateAPI(api_views.CreateAPIView):
    serializer_class = UserCarSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        user_car = UserCar(
            user=user,
            car_brand=serializer.validated_data['car_brand'],
            car_model=serializer.validated_data['car_model'],
        )

        user_car.full_clean()
        user_car.save()

        return Response(status=status.HTTP_200_OK)
