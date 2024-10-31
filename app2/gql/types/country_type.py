from graphene import ObjectType, Int, String, List, Field


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()

    cities = Field('app2.gql.types.city_type.CityType')
