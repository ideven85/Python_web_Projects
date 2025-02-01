from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from core.user import models
from core.user.models import Profile


# Register your models here.


# todo Need to modify admin interface to display both email and username fields.. building own is a waste of time..
@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ["email", "username", "first_name", "last_name", "is_staff"]
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']
    raw_id_fields = ['user']