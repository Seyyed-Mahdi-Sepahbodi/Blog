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
        exclude = ['id', 'author', 'status', 'created_at', 'updated_up', 'promote', 'slug']

    def get_category(self, instance):
        if instance.category:
            return instance.category.title
        return None


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('id', 'author', 'status', 'created_at', 'promote', 'slug')

    def create(self, validated_data):
        new_post = Post()
        new_post.title = validated_data['title']
        new_post.short_description = validated_data['short_description']
        new_post.cover = validated_data['cover']
        new_post.body = validated_data['body']
        new_post.category = validated_data['category']
        new_post.author = self.context['request'].user
        new_post.study_time = validated_data['study_time']
        new_post.status = 'PEN'
        new_post.save()

        return new_post

