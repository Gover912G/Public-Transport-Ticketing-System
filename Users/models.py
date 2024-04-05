from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    is_passenger = models.BooleanField(default = False)
    is_conductor = models.BooleanField(default = False)
    is_Owner = models.BooleanField(default = False)
    phone_number = models.CharField(max_length=15, blank=True, default=254791995308)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50)
    profil_pic = models.ImageField(null=True,default='images/profile.jpg',blank=True,upload_to='profile')

    def __str__(self):
        return self.user.username

# create a user profile automatically oncethey are registered
def create_profile(sender, instance, created, **kwags):
    if created:
        user_profile= Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile,sender=User)