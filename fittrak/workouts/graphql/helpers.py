"""
Workout GraphQL helpers
"""

from graphql import GraphQLError


def get_object(Model, options={}):
    try:
        obj = Model.objects.get(is_active=True, **options)
    except Model.DoesNotExist:
        raise GraphQLError("No matching {} found.".format(Model.__name__))
    except Model.MultipleObjectsReturned:
        raise GraphQLError("Multiple {} found.".format(Model.__name__))

    return obj
