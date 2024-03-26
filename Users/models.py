from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_passenger = models.BooleanField(default = False)
    is_conductor = models.BooleanField(default = False)
    is_Owner = models.BooleanField(default = False)
    # phone_number = models.CharField(max_length=15, blank=True, default='')
    # phone_number = models.CharField(max_length=15, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, default=254791995308)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASACADE)
    phone_number = models.CharField(max_length=15, blank=True, default=254791995308)
    image = models.ImageField(upload_to='profile_pictures')