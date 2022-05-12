from django.urls import path

from cars_restapi.cars_api.views import CarBrandListView, SingleCarBrandView, CarModelListView, SingleCarModelView

urlpatterns = (
    path('car-brands/', CarBrandListView.as_view(), name='car brands'),
    path('car-brands/<int:pk>', SingleCarBrandView.as_view(), name='single car brand'),
    path('car-models/', CarModelListView.as_view(), name='car models'),
    path('car-models/<int:pk>', SingleCarModelView.as_view(), name='single car model'),
)
