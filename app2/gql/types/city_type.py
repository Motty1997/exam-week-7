from graphene import ObjectType, Int, String, Float, List, Field


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()

    cities = Field('app2.gql.types.city_type.CityType')
