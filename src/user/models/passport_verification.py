from django.db import models

from core.utils.base_model import BaseModel
from file.models import File


class PassportVerification(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='passport_verification')
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255, unique=True)
    pinfl = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.serial_number
