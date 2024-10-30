from returns.result import Result, Success, Failure
from app.db.database import session_maker
from app.db.models import UserDetails


def create_user(user: UserDetails) -> Result[UserDetails, str]:
    with session_maker() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def create_users(users):
    with session_maker() as session:
        try:
            session.add_all(users)
            session.commit()
            return Success(True)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_all_users(root):
    with session_maker() as session:
        return session.query(UserDetails).all()
