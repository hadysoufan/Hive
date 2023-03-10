from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(
        upload_to='profileImg', default='default.png')
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user.username)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='postImages')
    caption = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now)
    numOfLikes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
