from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.dispatch import Signal

profile_updated = Signal()


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        print('Profile Signal Triggered')
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            name=user.first_name,
            email=user.email,
        )
        profile.save()
        print(f'username: {user.username}')
        print(f'name: {user.first_name}')
        print(f'email: {user.email}')


# @receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        print('created user triggered...')
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        print(f'user name: {user.first_name}')
        print(f'user username: {user.username}')
        print(f'user email: {user.email}')

    # Check if user exists in the admin panel
    if User.objects.filter(id=user.id).exists():
        print('existed user triggered...')
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.bio = profile.bio
        user.profileImg = profile.profileImg
        user.save()
        print(f'Profile bio: {profile.bio}')
        print(f'User bio: {user.bio}')
        print(f'User id:{user.id}')
        print(f'user profileImg: {user.profileImg}')

        # Send signal to update HTML form
        profile_updated.send(sender=Profile, user=user)


def deleteProfile(sender, instance, **kwargs):
    print('Profile Deleted')
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)
