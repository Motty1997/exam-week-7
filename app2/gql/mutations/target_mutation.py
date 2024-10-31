from graphene import Field, Int

from app.db.database import session_maker
from app2.db.models import Target
from app2.gql.mutations.mutation import Mutation


class CreateTarget(Mutation):
    class Arguments:
        a = Int()

    target = Field(Target)

    @staticmethod
    def create_mission(root, info, target):
        new_target = Target(**target)
        with session_maker() as session:
            session.add(new_target)
            session.commit()
            session.refresh(new_target)
            return CreateTarget(employee=new_target)