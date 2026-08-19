from .views import (
    RegisterAPIView,
    LoginAPIView,
    ProfileAPIView,
    ProfileUpdateAPI,
    ChangePasswordAPIView,
    LogoutAPIView,
)
from django.urls import path

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("profile/update", ProfileUpdateAPI.as_view(), name="profile/update"),
    path("change-password", ChangePasswordAPIView.as_view(), name="change-password"),
]
