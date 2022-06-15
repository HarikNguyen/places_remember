from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

def upload_avatar(instance,filename):
    filename = filename[-4:]
    path = 'users/'+instance.username +'_{filename}'
    return path.format(filename=filename)


class UserWithAvatar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_avatar,blank=True)

    def __str__(self):
        return f'Avatar for user {self.user.username}'