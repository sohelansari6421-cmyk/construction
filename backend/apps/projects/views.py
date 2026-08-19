from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import (
    ProjectSerializer,
    ProjectCreateUpdateSerializer,
    ProjectProgressSerializer,
    ProjectProgressCreateUpdateSerializer,
    ProjectProgressImageSerializer,
    ProjectProgressVideoSerializer,
)
from .models import Project, ProjectProgress, ProjectProgressImage, ProjectProgressVideo
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = [
        "title",
        "location",
        "description",
    ]

    filterset_fields = [
        "status",
        "featured",
        "service",
    ]
    ordering_fields = [
        "created_at",
        "title",
        "start_date",
    ]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer
        return ProjectCreateUpdateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer
        return ProjectCreateUpdateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ProjectProgressListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectProgress.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectProgressSerializer
        return ProjectProgressCreateUpdateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ProjectProgressRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = ProjectProgress.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectProgressSerializer
        return ProjectProgressCreateUpdateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ProjectProgressImageCreateAPIView(generics.CreateAPIView):
    queryset = ProjectProgressImage.objects.all()
    serializer_class = ProjectProgressImageSerializer
    permission_classes = [IsAdminUser()]


class ProjectProgressVideoCreateAPIView(generics.CreateAPIView):
    queryset = ProjectProgressVideo.objects.all()
    serializer_class = ProjectProgressVideoSerializer
    permission_classes = [IsAdminUser()]
