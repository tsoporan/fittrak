"""Root GraphQL Schema"""

import graphene
from graphene_django.debug import DjangoDebug
from users.schema import Query as UsersQuery
from workouts.graphql.exercises import (AddCustomExercise, AddExercises,
                                        RemoveExercise)
from workouts.graphql.schema import Query as WorkoutsQuery
from workouts.graphql.sets import AddSet, RemoveSet, UpdateSet
from workouts.graphql.workouts import (CreateWorkout, RemoveWorkout,
                                       UpdateWorkout)


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


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
