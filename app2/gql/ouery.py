from graphene import ObjectType, List, Date, String
from app2.gql.types.mission_type import MissionType
from app2.repository.mission_repository import get_missions_between_days, get_mission_by_country, \
    get_mission_by_target_industry, get_mission_by_target_type


class Query(ObjectType):
    missions_between_days = List(MissionType, start=Date(), end=Date())
    mission_by_country = List(MissionType, country_name=String())
    mission_by_target_industry = List(MissionType, industry=String())
    mission_by_target_type = List(MissionType, target_type=String())


    @staticmethod
    def resolve_missions_between_days(root, info, start, end):
        return get_missions_between_days(start, end)

    @staticmethod
    def resolve_mission_by_country(root, info, country_name):
        return get_mission_by_country(country_name)

    @staticmethod
    def resolve_mission_by_target_industry(root, info, industry):
        return get_mission_by_target_industry(industry)

    @staticmethod
    def resolve_mission_by_target_type(root, info, target_type):
        return get_mission_by_target_type(target_type)
