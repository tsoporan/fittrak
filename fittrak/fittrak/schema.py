"""Root GraphQL Schema"""

import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from workouts.schema import CreateWorkout, RemoveWorkout, Query as WorkoutsQuery
from users.schema import Query as UsersQuery


class RootQuery(WorkoutsQuery, UsersQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class RootMutation(graphene.ObjectType):
    create_workout = CreateWorkout.Field()
    remove_workout = RemoveWorkout.Field()

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
