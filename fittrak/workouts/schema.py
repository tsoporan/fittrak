"""Workouts GraphQL schema"""

import graphene

from django.utils import timezone

from graphql import GraphQLError

from graphene_django.types import DjangoObjectType

from .models import Workout, Exercise, ExerciseType as ExerciseTypeModel, Set

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class ExerciseType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = Exercise

    def resolve_name(instance, info):
        return instance.exercise_type.name


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class Query:
    all_workouts = graphene.List(WorkoutType)
    all_exercises = graphene.List(ExerciseType)
    all_sets = graphene.List(SetType)

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()

    def resolve_all_sets(self, info, **kwargs):
        return Set.objects.all()


class AddExercise(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_name = graphene.String(required=True)

    workout = graphene.Field(WorkoutType)
    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, workout_id, exercise_name):
        user = info.context.user

        try:
            workout = Workout.objects.get(id=workout_id, user=user)
        except Workout.DoesNotExist:
            raise GraphQLError("No matching workout.")

        # Allows for users to define their own exercise types based on name
        exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
            user=user,
            name=exercise_name
        )

        exercise = Exercise.objects.create(
            user=user,
            workout=workout,
            exercise_type=exercise_type,
            date_started = timezone.now()
        )

        return AddExercise(workout=workout, exercise=exercise)


class CreateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    def mutate(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not authenticated.")

        new_workout = Workout.objects.create(
            user = user,
            date_started = timezone.now()
        )

        return CreateWorkout(workout=new_workout)


class RemoveWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)

    def mutate(self, info, workout_id):
        user = info.context.user

        try:
            workout = Workout.objects.get(id=workout_id, user=user)
        except Workout.DoesNotExist:
            raise GraphQLError("No matching workout.")

        workout.is_active = False
        workout.save()

        return RemoveWorkout(workout=workout)
