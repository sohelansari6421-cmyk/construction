from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    ProjectProgressRetrieveUpdateDestroyAPIView,
    ProjectProgressListCreateAPIView,
    ProjectProgressImageCreateAPIView,
    ProjectProgressVideoCreateAPIView,
)

from django.urls import path

urlpatterns = [
    # projects
    path(
        "projects/",
        ProjectListCreateAPIView.as_view(),
        name="project-list-create",
    ),
    path(
        "projects/<slug:slug>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
    # project Proress
    path(
        "projects/progress/",
        ProjectProgressListCreateAPIView.as_view(),
        name="project-progress-list-create",
    ),
    path(
        "projects/progress/<int:pk>/",
        ProjectProgressRetrieveUpdateDestroyAPIView.as_view(),
        name="project-progress-detail",
    ),
    # upload image and vedios
    path(
        "projects/progress/images/",
        ProjectProgressImageCreateAPIView.as_view(),
        name="project-progress-Image-create",
    ),
    path(
        "projects/progress/vedios/",
        ProjectProgressVideoCreateAPIView.as_view(),
        name="project-progress-vedios-created",
    ),
]
