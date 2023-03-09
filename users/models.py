from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(
        upload_to='profileImg', default='default.png')
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
