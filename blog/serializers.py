from rest_framework import serializers
from .models import Post


class AllPostsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ('body', 'slug', 'created_at')

    def get_category(self, instance):
        if instance.category:
            return instance.category.title
        return None

    def get_author(self, instance):
        if instance.author.get_full_name() != "":
            return instance.author.get_full_name()
        return instance.author.username

    def get_status(self, instance):
        if instance.status == 'PUB':
            return 'منتشر شده'
        elif instance.status == 'DRF':
            return 'پیش نویس'
        elif instance.status == 'PEN':
            return 'در صف تایید'
        return 'حذف شده'


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ['id', 'author', 'status', 'created_at', 'promote', 'slug']

    def get_category(self, instance):
        if instance.category:
            return instance.category.title
        return None
