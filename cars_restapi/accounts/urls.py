from django.urls import path

from cars_restapi.accounts.views import RegisterView, LoginView, LogoutView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
    path('register/', LogoutView.as_view(), name='logout user'),
)
