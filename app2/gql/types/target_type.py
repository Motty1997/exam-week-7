from graphene import ObjectType, Int, String, Field



class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    city = Field('app2.gql.types.city_type.CityType')
    mission = Field('app2.gql.types.mission_type.MissionType')
    target_type = Field('app2.gql.types.target_type.TargetType')
