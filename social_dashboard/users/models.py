from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add fields for social media integration if needed
    bio = models.TextField(blank=True, null=True)
