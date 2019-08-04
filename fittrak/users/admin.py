from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "verification_token", "created_at", "updated_at")
    search_fields = ("user__email", "user__username")
    date_hierarchy = "created_at"


admin.site.register(User, UserAdmin)
