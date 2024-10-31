from app.db.database import session_maker


def create_target(target):
    with session_maker() as session:
        session.add(target)
        session.commit()
        session.refresh(target)
        return target
