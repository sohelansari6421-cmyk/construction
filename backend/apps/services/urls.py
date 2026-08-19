from django.urls import path
from .views import (
    ServiceCreateAPIView,
    ServiceListAPIView,
    ServiceDeleteAPIView,
    ServiceDetailAPIView,
    ServiceUpdateAPIView,
)

urlpatterns = [
    path("service/", ServiceListAPIView.as_view(), name="service"),
    path("service/<int:id>/", ServiceDetailAPIView.as_view(), name="detail"),
    path("service/<int:id>/", ServiceCreateAPIView.as_view(), name="create"),
    path("service/<int:id>/", ServiceUpdateAPIView.as_view(), name="update"),
    path("service/<int:id>/", ServiceDeleteAPIView.as_view(), name="delete"),
]
