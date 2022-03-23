from datetime import datetime

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import format_html

# Create your models here.

user = get_user_model()

def post_cover_path(instance, filename):
    path = f'post/cover/{instance.title}/{filename}'
    return path

def category_cover_path(instance, filename):
    path = f'category/cover/{instance.title}/{filename}'
    return path

def validate_file_extension(value):
    import os

    from django.core.exceptions import ValidationError
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension!')

class Post(models.Model):
    PUBLISHED = 'PUB'
    DRAFT = 'DRF'
    PENDING = 'PEN'
    REMOVED = 'RMV'
    POST_STATUS_CHOICES = [
        (PUBLISHED, 'منتشر شده'),
        (DRAFT, 'کامل نشده'),
        (PENDING, 'در صف تایید'),
        (REMOVED, 'حدف شده')
    ]
    title = models.CharField(max_length=100, verbose_name='عنوان')
    short_description = models.CharField(max_length=255, verbose_name='خلاصه')
    cover = models.ImageField(upload_to=post_cover_path, blank=True, null=True, validators=[validate_file_extension], verbose_name='تصویر')
    body = RichTextField(verbose_name='محتوا')
    author = models.ForeignKey(user, on_delete=models.DO_NOTHING, verbose_name='نویسنده')
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True, verbose_name='کد صفحه')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, related_name='category_posts', verbose_name='دسته بندیها')
    # tag = models.ManyToManyField('blog.Tag', verbose_name='تگ ها', related_name='tag_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateField(auto_now=True, verbose_name='زمان بروزرسانی')
    study_time = models.IntegerField(null=True, verbose_name='مدت زمان تقریبی مطالعه')
    status = models.CharField(max_length=3, choices=POST_STATUS_CHOICES, default=DRAFT, verbose_name='وضعیت')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def filename(self):
        return os.path.basename(self.cover.name)

    def cover_tag(self):
        if self.cover:
            return format_html(f"<img src='{self.cover.url}' height='100px' width='100px' style='border-radius: 5px;'")
        return format_html("<p>-</p>")
    cover_tag.short_description = 'تصویر'

    def __str__(self):
        return self.title

    #     def jpublish(self):
#         return jalali_convertor(self.created_at)

    # def save(self, *args, **kwargs):
    #     if Post.objects.filter(slug=self.slug):
    #         extra = str(randint(1, 10000))
    #         self.slug = self.slug + "-" + extra
    #         print(self.slug)
    #     else:
    #         print("Errrrrrrror")
    #     # if not self.slug:
    #     #     if Post.objects.filter(title=self.title):
    #     #         extra = str(randint(1, 10000))
    #     #         self.slug = slugify(self.title) + "-" + extra
    #     #     else:
    #     #         self.slug = slugify(self.title)
    #     print(self.slug)
    #     super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان')
    cover = models.ImageField(upload_to=category_cover_path, null=True, blank=True, validators=[validate_file_extension], verbose_name='تصویر')
    short_description = models.TextField(verbose_name='توضیح مختصر')
    parent = models.ForeignKey('self', name='child', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته‌بندی مرجع')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایحاد')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندیها'

    def cover_tag(self):
        return format_html(f"<img src='{self.cover.url}' height='100px' width='100px' style='border-radius: 5px;'")
    cover_tag.short_description = 'تصویر'

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(user, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, verbose_name='پست')
    body = models.TextField(verbose_name='محتوا')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.author.username + "-" + self.created_at.strftime("%m/%d/%Y-%H:%M:%S")
