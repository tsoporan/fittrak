import graphene

from graphene_django.types import DjangoObjectType

from workouts.models import Workout, Exercise


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise


class Query(object):
    all_workouts = graphene.List(WorkoutType)
    all_exercises = graphene.List(ExerciseType)

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()
