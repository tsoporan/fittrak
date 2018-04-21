"""GraphQL Schema"""

import graphene

import workouts.schema


class Query(workouts.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
