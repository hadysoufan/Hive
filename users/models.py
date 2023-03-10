from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import uuid

# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(
        upload_to='media', default='default.png')
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user.username)


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


# @receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    print('user deleted')


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteProfile, sender=Profile)
