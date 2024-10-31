from graphene import ObjectType
from app2.gql.mutations.mission_mutate import CreateMission, UpdateMission, DeleteMission


class Mutation(ObjectType):
    createMission = CreateMission.Field()
    updateMission = UpdateMission.Field()
    deleteMission = DeleteMission.Field()
