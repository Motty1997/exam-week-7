from graphene import Field

from graphene import ObjectType, Int, String



class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    target = Field("app2.gql.types.target_type.TargetType")
