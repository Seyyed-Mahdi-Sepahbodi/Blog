from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from blog.validators import validate_file_extension
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.

def user_profile_avatar_path(instance, filename):
    path = f'upload/user_profile/avatars/{instance.user.username}/{filename}'
    return path

class CustomUser(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    special_user = models.DateTimeField(default=timezone.now, verbose_name='کاربر ویژه تا')
    age = models.SmallIntegerField(null=True)

    def get_user_full_name(self):
        return self.first_name + " " + self.last_name

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        return False
    is_special_user.boolean = True
    is_special_user.short_description = 'وضعیت کاربر ویژه'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofiles', verbose_name='کاربر')
    avatar = models.FileField(upload_to=user_profile_avatar_path, null=True, blank=True, validators=[validate_file_extension], verbose_name='آواتار')
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