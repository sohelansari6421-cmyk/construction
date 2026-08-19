from rest_framework import serializers
from .models import Project, ProjectProgress, ProjectProgressImage, ProjectProgressVideo
from apps.services.serializers import ServiceSerializer


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "description",
            "location",
            "thumbnail",
            "start_date",
            "expected_end_date",
            "actual_end_date",
            "service",
            "status",
            "featured",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class ProjectProgressImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectProgressVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectProgressSerializer(serializers.ModelSerializer):
    images = ProjectProgressImageSerializer(many=True, read_only=True)
    videos = ProjectProgressVideoSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectProgress
        fields = "__all__"


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectProgressCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgress
        fields = "__all__"
