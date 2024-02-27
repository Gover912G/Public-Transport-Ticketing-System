from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_passenger = models.BooleanField(default = False)
    is_conductor = models.BooleanField(default = False)
    is_Owner = models.BooleanField(default = False)

    def __str__(self):
        return self.username