from django.contrib import admin
from .models import Workout, Exercise, Set

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ('user__email', 'slug')
    date_hierarchy = 'date_started'
    list_display = ('slug', 'user', 'date_started', 'date_ended', 'is_active')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ('user__email', 'name', 'slug', 'workout__slug')
    date_hierarchy = 'date_started'
    list_display = ('name', 'slug', 'user', 'workout', 'date_started', 'date_ended', 'is_active')

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    search_fields = ('exercise__name', 'user__email')
    date_hierarchy = 'date_started'
    list_display = ('exercise', 'repetitions', 'user', 'date_started', 'date_ended', 'is_active')
