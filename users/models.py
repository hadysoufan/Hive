from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.


class Profile(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(
        upload_to='profiles/', default='profiles/default.png', null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user.username)
