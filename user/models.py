from django.db import models
from django.contrib.auth.models import User
from blog.models import validate_file_extension
from django.utils.html import format_html


# Create your models here.

def user_profile_avatar_path(instance, filename):
    path = f'upload/user_profile/avatars/{instance.user.username}/{filename}'
    return path

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.FileField(upload_to=user_profile_avatar_path, validators=[validate_file_extension], verbose_name='آواتار')
    description = models.CharField(max_length=512, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'پروفایل کاربری'
        verbose_name_plural = 'پروفایل‌های کاربران'

    def filename(self):
        return os.path.basename(self.avatar.name)

    def avatar_tag(self):
        return format_html(f"<img src='{self.avatar.url}' height='100px' width='100px' style='border-radius: 5px;'")
    avatar_tag.short_description = 'تصویر'

    def __str__(self):
        return self.user.username