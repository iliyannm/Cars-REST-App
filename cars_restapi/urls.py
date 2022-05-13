from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars_restapi.cars_api.urls')),
    path('accounts/', include('cars_restapi.accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
