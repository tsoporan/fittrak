"""
Users GraphQL mutations
"""

import graphene

from .types import UnitEnumType, Viewer


class UpdateSettings(graphene.Mutation):
    viewer = graphene.Field(Viewer)

    class Arguments:
        height = graphene.Float(default_value=None)
        weight = graphene.Float(default_value=None)
        preferred_unit = graphene.Argument(UnitEnumType, required=True)

    @staticmethod
    def mutate(_, info, preferred_unit, **kwargs):

        # Optional fields are not passed to mutate ...
        height = kwargs.pop("height", None)
        weight = kwargs.pop("weight", None)

        user = info.context.user
        profile = user.profile

        profile.height = height
        profile.weight = weight
        profile.preferred_unit = preferred_unit

        profile.save()

        return UpdateSettings(viewer=profile.user)
