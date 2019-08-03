"""Root GraphQL Schema"""

import graphene
from graphene_django.debug import DjangoDebug

from users.graphql.mutations import UpdateSettings
from users.graphql.query import Query as UsersQuery
from workouts.graphql.mutations import (
    AddCustomExercise,
    AddExercises,
    AddSet,
    CreateWorkout,
    RemoveExercise,
    RemoveSet,
    RemoveWorkout,
    UpdateSet,
    UpdateWorkout,
)
from workouts.graphql.query import Query as WorkoutsQuery


class RootQuery(WorkoutsQuery, UsersQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


class RootMutation(graphene.ObjectType):
    create_workout = CreateWorkout.Field()
    remove_workout = RemoveWorkout.Field()
    update_workout = UpdateWorkout.Field()
    add_exercises = AddExercises.Field()
    add_custom_exercise = AddCustomExercise.Field()
    remove_exercise = RemoveExercise.Field()
    add_set = AddSet.Field()
    remove_set = RemoveSet.Field()
    update_set = UpdateSet.Field()
    update_settings = UpdateSettings.Field()


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
