from django.contrib import admin

from .models import Exercise, ExerciseType, Set, Workout, WorkoutEvent


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ("user__email", "user__username", "slug")
    date_hierarchy = "started_at"
    list_display = (
        "id",
        "slug",
        "user",
        "status",
        "started_at",
        "ended_at",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "status", "created_at")


@admin.register(ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", "user__email", "user__username")
    list_display = ("id", "user", "name", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    date_hierarchy = "created_at"


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "id",
        "user",
        "weight",
        "repetitions",
        "unit",
        "bodyweight",
        "exercise",
        "is_active",
    )
    list_filter = ("created_at", "is_active")


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
    date_hierarchy = "created_at"
    list_display = (
        "id",
        "get_type",
        "slug",
        "workout",
        "started_at",
        "ended_at",
        "created_at",
        "is_active",
    )
    list_filter = ("created_at", "is_active")
    inlines = [SetInline]

    @staticmethod
    def get_type(obj):
        return obj.exercise_type.name if hasattr(obj, "exercise_type") else "N/A"

    get_type.short_description = "Type"


@admin.register(WorkoutEvent)
class WorkoutEventAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("id", "user", "workout", "created_at", "action")
    list_filter = ("action", "is_active")
    search_fields = ("user__email", "user__username", "workout__slug")
