from graphene import InputObjectType, Int, Date, Float, Field
from app2.db.database import session_maker
from app2.db.models.mission import Mission
from app2.gql.mutations.mutation import Mutation
from app2.gql.types.mission_type import MissionType
from app2.repository.mission_repository import update_mission, delete_mission


class MissionInput(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()


class CreateMission(Mutation):
    class Arguments:
        missionInput = MissionInput()

    mission = Field(MissionType)

    @staticmethod
    def create_mission(root, info, mission):
        new_mission = Mission(**mission)
        with session_maker() as session:
            session.add(new_mission)
            session.commit()
            session.refresh(new_mission)
            return CreateMission(employee=new_mission)

class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost):
        return UpdateMission(
            mission=update_mission(mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost))


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        return DeleteMission(student=delete_mission(mission_id))
