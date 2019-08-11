"""
Workout GraphQL mutations
"""

from copy import deepcopy

import graphene
from django.utils import timezone
from graphql import GraphQLError

from workouts.helpers import create_workout_event
from workouts.models import Exercise
from workouts.models import ExerciseType as ExerciseTypeModel
from workouts.models import MuscleGroup, Set, Workout

from .types import (
    ExerciseInputType,
    ExerciseType,
    SetFieldInputType,
    SetType,
    WorkoutFieldInputType,
    WorkoutType,
)


class CreateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    @staticmethod
    def mutate(_, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not authenticated.")

        new_workout = Workout.objects.create(user=user)

        create_workout_event(user=user, action="create_workout", workout=new_workout)

        return CreateWorkout(workout=new_workout)


class RemoveWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)

    @staticmethod
    def mutate(_, info, workout_id):
        user = info.context.user

        try:
            workout = Workout.objects.get(is_active=True, id=workout_id, user=user.id)
        except Workout.DoesNotExist:
            raise GraphQLError("Workout not found.")

        workout.is_active = False
        workout.status = Workout.ARCHIVED
        workout.save(update_fields=["is_active", "status"])

        create_workout_event(user=user, action="remove_workout", workout=workout)

        return RemoveWorkout(workout=workout)


class UpdateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)
        workout_fields = graphene.Argument(WorkoutFieldInputType, required=True)

    @staticmethod
    def mutate(_, info, workout_id, workout_fields):
        user = info.context.user

        try:
            workout = Workout.objects.get(is_active=True, id=workout_id, user=user.id)
        except Workout.DoesNotExist:
            raise GraphQLError("Workout not found.")

        before_workout = deepcopy(workout)

        dirty = False

        # Must happen before as exercises require special handling
        # TODO: Separate concerns?
        exercise_types = workout_fields.pop("exercise_types", None)

        if exercise_types:
            dirty = True

            types = ExerciseTypeModel.objects.filter(
                id__in=[e.id for e in exercise_types]
            )

            for exercise_type in types:
                Exercise.objects.get_or_create(
                    workout=workout, exercise_type=exercise_type, user=user
                )

        # Unpack the fields and update the model

        for field_name, value in workout_fields.items():
            if not hasattr(workout, field_name):
                continue

            setattr(workout, field_name, value)

            dirty = True

        if dirty:
            workout.save()

            create_workout_event(
                user=user,
                action="update_workout",
                workout=workout,
                state={"before_workout": before_workout, "after_workout": workout},
            )

        return UpdateWorkout(workout=workout)


class AddCustomExercise(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_name = graphene.String(required=True)
        muscle_group_name = graphene.String(required=True)

    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, workout_id, exercise_name, muscle_group_name):
        user = info.context.user

        muscle_group = MuscleGroup.objects.get(name=muscle_group_name)

        exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
            user=user, name=exercise_name, muscle_group=muscle_group
        )

        workout = Workout.objects.get(id=workout_id)

        exercise = Exercise.objects.create(
            user=user, workout=workout, exercise_type=exercise_type
        )

        create_workout_event(
            user=user,
            action="add_custom_exercise_to_workout",
            workout=workout,
            state={
                "exericse": exercise,
                "exercise_type": exercise_type,
                "muscle_group": muscle_group,
            },
        )

        return AddCustomExercise(exercise=exercise)


class AddExercises(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercises = graphene.List(ExerciseInputType, required=True)

    workout = graphene.Field(WorkoutType)
    exercises = graphene.List(ExerciseType)

    @staticmethod
    def mutate(_, info, workout_id, exercises):
        user = info.context.user

        try:
            workout = Workout.objects.get(is_active=True, id=workout_id, user=user.id)
        except Workout.DoesNotExist:
            raise GraphQLError("Workout not found.")

        added = []

        for exercise in exercises:
            name = exercise["name"]

            # Allows for users to define their own exercise types based on name
            exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
                user=user, name=name
            )

            exercise = Exercise.objects.create(
                user=user,
                workout=workout,
                exercise_type=exercise_type,
                started_at=timezone.now(),
            )

            added.append(exercise)

        create_workout_event(
            user=user,
            action="add_exercises_to_workout",
            workout=workout,
            state={"exercises": added},
        )

        return AddExercises(workout=workout, exercises=added)


class RemoveExercise(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)

    workout = graphene.Field(WorkoutType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, exercise_id):
        user = info.context.user

        try:
            exercise = Exercise.objects.get(
                is_active=True, id=exercise_id, user=user.id
            )
        except Exercise.DoesNotExist:
            raise GraphQLError("Exercise not found.")

        workout = exercise.workout

        exercise.is_active = False
        exercise.save()

        create_workout_event(
            user=user,
            action="remove_exercise_from_workout",
            workout=workout,
            state={"exercise": exercise},
        )

        return RemoveExercise(exercise=exercise, workout=workout)


class AddSet(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)
        repetitions = graphene.Int(required=True)
        weight = graphene.Decimal(required=True)
        unit = graphene.String(required=True)
        bodyweight = graphene.Boolean(default_value=False)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, exercise_id, repetitions, weight, unit, bodyweight):
        user = info.context.user

        try:
            exercise = Exercise.objects.get(
                is_active=True, id=exercise_id, user=user.id
            )
        except Exercise.DoesNotExist:
            raise GraphQLError("Exercise not found.")

        if not exercise.workout:
            raise GraphQLError("Exercise does not belong to a workout.")

        _set = Set.objects.create(
            user=user,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight,
            unit=unit,
            bodyweight=bodyweight,
        )

        create_workout_event(
            user=user,
            action="add_set_to_workout",
            workout=exercise.workout,
            state={"set": _set, "exercise": exercise},
        )

        return AddSet(set=_set, exercise=exercise)


class UpdateSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)
        set_fields = graphene.Argument(SetFieldInputType, required=True)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, set_id, set_fields):
        user = info.context.user

        try:
            _set = Set.objects.get(is_active=True, id=set_id, user=user.id)
        except Set.DoesNotExist:
            raise GraphQLError("Set not found.")

        dirty = False

        before_set = deepcopy(_set)

        for name, value in set_fields.items():
            if not hasattr(_set, name):
                continue

            setattr(_set, name, value)

            dirty = True

        if dirty:
            _set.updated_at = timezone.now()
            _set.save()

        create_workout_event(
            user=user,
            action="update_set_on_workout",
            workout=_set.exercise.workout,
            state={
                "before_set": before_set,
                "after_set": _set,
                "exercise": _set.exercise,
            },
        )

        return UpdateSet(set=_set, exercise=_set.exercise)


class RemoveSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, set_id):
        user = info.context.user

        try:
            _set = Set.objects.get(is_active=True, id=set_id, user=user.id)
        except Set.DoesNotExist:
            raise GraphQLError("Set not found.")

        _set.is_active = False
        _set.updated_at = timezone.now()
        _set.save()

        create_workout_event(
            user=user,
            action="remove_set_from_workout",
            workout=_set.exercise.workout,
            state={"set": _set, "exercise": _set.exercise},
        )

        return RemoveSet(set=_set, exercise=_set.exercise)
