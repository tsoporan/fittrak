"""Workouts GraphQL schema"""

from django.utils import timezone

import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType

from .models import Workout, Exercise, ExerciseType as ExerciseTypeModel, Set


def get_object(Model, options={}):
    try:
        obj = Model.objects.get(
            is_active=True,
            **options
        )
    except Model.DoesNotExist:
        raise GraphQLError("No matching {} found.".format(Model.__name__))
    except Model.MultipleObjectsReturned:
        raise GraphQLError("Multiple {} found.".format(Model.__name__))

    return obj


class WorkoutFieldInputType(graphene.InputObjectType):
    date_ended = graphene.types.datetime.DateTime()


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

    exercise = graphene.Field(ExerciseType,
        exercise_id=graphene.Int(required=True)
    )

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()

    def resolve_all_sets(self, info, **kwargs):
        return Set.objects.all()

    def resolve_exercise(self, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        return exercise


class AddExercise(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_name = graphene.String(required=True)

    workout = graphene.Field(WorkoutType)
    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, workout_id, exercise_name):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

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


class AddSet(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)
        repetitions = graphene.Int(required=True)
        weight = graphene.Int(required=True)
        unit = graphene.String()

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)
    workout = graphene.Field(WorkoutType)

    def mutate(self, info, exercise_id, repetitions, weight, unit):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        if not exercise.workout:
            raise GraphQLError("Exercise does not belong to a workout.")

        set = Set.objects.create(
            user=user,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight
        )

        return AddSet(set=set, exercise=exercise, workout=exercise.workout)

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

        workout = get_object(Workout, {"id": workout_id, "user": user.id})
        workout.is_active = False
        workout.save()

        return RemoveWorkout(workout=workout)


class UpdateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)
        workout_fields = graphene.Argument(
            WorkoutFieldInputType,
            required=True
        )

    def mutate(self, info, workout_id, workout_fields):
        user = info.context.user
        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        dirty = False
        # Unpack the fields and update the model
        for name, value in workout_fields.items():
            if not hasattr(workout, name):
                continue

            setattr(workout, name, value)
            dirty = True

        if dirty:
            workout.save()

        return UpdateWorkout(workout=workout)
