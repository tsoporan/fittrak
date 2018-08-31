"""Root GraphQL Schema"""

import graphene

from graphene_django.debug import DjangoDebug

from workouts.graphql.schema import Query as WorkoutsQuery

from workouts.graphql.workouts import CreateWorkout, RemoveWorkout, UpdateWorkout
from workouts.graphql.exercises import AddExercises, RemoveExercise
from workouts.graphql.sets import AddSet, RemoveSet, UpdateSet

from users.schema import Query as UsersQuery


class RootQuery(WorkoutsQuery, UsersQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


class RootMutation(graphene.ObjectType):
    create_workout = CreateWorkout.Field()
    remove_workout = RemoveWorkout.Field()
    update_workout = UpdateWorkout.Field()
    add_exercises = AddExercises.Field()
    remove_exercise = RemoveExercise.Field()
    add_set = AddSet.Field()
    remove_set = RemoveSet.Field()
    update_set = UpdateSet.Field()


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
