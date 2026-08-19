from django.contrib import admin
from .models import (
    Service,
    Project,
    ProjectProgress,
    ProjectProgressVideo,
    ProjectProgressImage,
)

# Register your models here.
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectProgress)
admin.site.register(ProjectProgressVideo)
admin.site.register(ProjectProgressImage)
