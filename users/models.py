from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(
        upload_to='media', default='default.png')
    location = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.username)
