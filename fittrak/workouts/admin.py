from django.contrib import admin

from .models import Exercise, ExerciseType, Set, Workout, WorkoutEvent


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ("user__email", "user__username", "slug")
    date_hierarchy = "date_started"
    list_display = (
        "id",
        "slug",
        "user",
        "status",
        "date_started",
        "date_ended",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "status", "created_at")


@admin.register(ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", "user__email", "user__username")
    list_display = ("id", "user", "name", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    date_hierarchy = "created_at"


class SetInline(admin.StackedInline):
    model = Set


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    search_fields = (
        "type__name",
        "slug",
        "workout__slug",
        "user__email",
        "user__username",
    )
    date_hierarchy = "date_started"
    list_display = (
        "id",
        "get_type",
        "slug",
        "workout",
        "date_started",
        "date_ended",
        "is_active",
    )
    list_filter = ("created_at", "is_active")
    inlines = [SetInline]

    @staticmethod
    def get_type(obj):
        if not hasattr(obj, "exercise_type"):
            return "N/A"

        return obj.exercise_type.name

    get_type.short_description = "Type"


@admin.register(WorkoutEvent)
class WorkoutEventAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("id", "user", "workout", "created_at", "action")
    list_filter = ("action", "is_active")
    search_fields = ("user__email", "user__username", "workout__slug")
