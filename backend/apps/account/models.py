from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserRole(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    EMPLOYEE = "employee", "Employee"
    ADMIN = "admin", "Admin"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    user_role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
