from returns.result import Success, Failure
from app.db.database import session_maker
from app.db.models import Address


def create_addresses(addresses):
    with session_maker() as session:
        try:
            session.add_all(addresses)
            session.commit()
            return Success(True)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_all_addresses(root):
    with session_maker() as session:
        return session.query(Address).all()
