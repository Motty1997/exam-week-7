from graphene import ObjectType, Int, Date, Float, Field


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damage = Float()
    aircraft_lost = Float()

    targets = Field('app2.gql.types.target_type.TargetType')
