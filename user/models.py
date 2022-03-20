from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_profile_avatar_path(instance, filename):
    path = f'upload/user_profile/avatars/{instance.user.username}/{filename}'
    return path

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.FieldFile(upload_to=user_profile_avatar_path, verbose_name='آواتار')
    description = models.CharField(max_length='512', verbose_name='توضیحات')

    def filename(self):
        return os.path.basename(self.avatar.name)