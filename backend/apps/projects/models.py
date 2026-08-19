from django.db import models
from apps.services.models import Service

# Create your models here.
STATUS_CHOICES = [
    ("upcoming", "Upcoming"),
    ("ongoing", "Ongoing"),
    ("completed", "Completed"),
]


class Project(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="upcoming")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="projects"
    )
    short_description = models.CharField(max_length=225)
    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
    )
    start_date = models.DateField()
    expected_end_date = models.DateField(null=True, blank=True)

    actual_end_date = models.DateField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectProgress(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="progress_updates",
    )
    title = models.CharField(max_length=225)
    description = models.TextField()
    progress_percentage = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title}-{self.title}"


class ProjectProgressImage(models.Model):
    progress = models.ForeignKey(
        ProjectProgress,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="projects/progress/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image - {self.progress.title}"


class ProjectProgressVideo(models.Model):
    progress = models.ForeignKey(
        ProjectProgress,
        on_delete=models.CASCADE,
        related_name="videos",
    )
    video = models.FileField(upload_to="projects/videos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video -{self.progress.title}"
