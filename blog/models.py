from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


# Create your models here.

def post_cover_path(instance, filename):
    path = f'upload/post/cover/{instance.title}/{filename}'
    return path

def category_cover_path(instance, filename):
    path = f'upload/category/cover/{instance.title}/{filename}'
    return path

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
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان')
    short_description = models.CharField(max_length=255, verbose_name='خلاصه')
    cover = models.ImageField(upload_to=post_cover_path, blank=True, null=True, verbose_name='تصویر')
    body = models.TextField(verbose_name='متن')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='نویسنده')
    slug = models.SlugField(verbose_name='کد شماره صفحه', unique=True, null=True, blank=True)
    category = models.ManyToManyField('blog.Category', verbose_name='دسته بندیها', related_name='category_posts')
    # tag = models.ManyToManyField('blog.Tag', verbose_name='تگ ها', related_name='tag_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد', null=True)
    updated_at = models.DateField(auto_now=True, verbose_name='زمان بروزرسانی')
    study_time = models.IntegerField(null=True, verbose_name='مدت زمان تقریبی مطالعه')
    status = models.CharField(max_length=3, choices=POST_STATUS_CHOICES, default=DRAFT, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def filename(self):
        return os.path.basename(self.cover.name)

#     def jpublish(self):
#         return jalali_convertor(self.created_at)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            if Post.objects.filter(title=self.title).exists():
                extra = str(randint(1, 10000))
                self.slug = slugify(self.title) + "-" + extra
            else:
                self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, verbose_name='پست')
    body = models.TextField(verbose_name='محتوا')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.author.username + ":" + self.created_at.strftime()


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان')
    cover = models.ImageField(upload_to=category_cover_path, null=True, blank=True, verbose_name='تصویر')
    short_description = models.TextField(verbose_name='توضیح مختصر')
    parent = models.ForeignKey('self', name='child', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته‌بندی مرجع')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندیها'

    def image_tag(self):
        return format_html(f"<img src='{self.cover.url}' height='100px' width='100px' style='border-radius: 5px;'")
    image_tag.short_description = 'تصویر'

    def __str__(self):
        return self.title