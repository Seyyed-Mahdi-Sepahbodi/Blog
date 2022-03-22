from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'category', 'status', 'cover_tag']
    list_editable = ('status',)
    search_fields = ['title', 'body']
    list_filter = ('category', 'status')
    date_hierarchy = ('created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-created_at']
    fieldsets = (
        (None, {
            "fields": (
                'title',
                'short_description',
                'body',
                'cover',
                'category',
                'study_time',
                'status',
            ),
        }),
        ('advanced options', {
            'classes': ('collapse',),
            'fields': ('author', 'slug'),
        })
    )
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_tag')
    search_fields = ['title', 'short_description']
    list_filter = ('created_at',)
    date_hierarchy = ('created_at')
admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
admin.site.register(Comment)
