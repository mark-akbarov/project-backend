import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser

from file.models import File


class UserType(models.IntegerChoices):
    PASSENGER = 0, 'Passenger'
    DRIVER = 1, 'Driver'
    
  
class User(AbstractUser):
    username = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(max_length=12, null=True, unique=True)
    email = models.EmailField(max_length=255, null=True, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=100, choices=UserType.choices, default=UserType.PASSENGER)
    profile_picture = models.OneToOneField(File, on_delete=models.CASCADE, null=True)
    is_passport_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']
    
    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
