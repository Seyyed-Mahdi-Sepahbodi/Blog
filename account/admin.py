from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

UserAdmin.fieldsets[2][1]['fields'] = (
                                        "is_active",
                                        "is_staff",
                                        "is_superuser",
                                        "is_author",
                                        "special_user",
                                        "groups",
                                        "user_permissions",
                                    )
UserAdmin.list_display += ('is_author', 'is_special_user')
UserAdmin.add_fieldsets[0][1]['classes'] = ("wied",)
UserAdmin.add_fieldsets[0][1]['fields'] = ("first_name", "last_name", "username", 'email', "password1", "password2")

admin.site.register(CustomUser, UserAdmin) 


class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)