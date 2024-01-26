from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from PIL import Image


# Create your models here.

class StaffUser(AbstractUser):
    is_director = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default='Email address', unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=255)
    temporary_password = models.CharField(max_length=128, blank=True, null=True)

    def _str_(self):
        return self.username

    class Meta:
        db_table = 'transport_system_users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

