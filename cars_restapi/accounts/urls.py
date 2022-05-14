from django.urls import path

from cars_restapi.accounts.views import RegisterView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
)
