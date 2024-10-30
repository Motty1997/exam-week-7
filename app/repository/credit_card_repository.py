from returns.result import Success, Failure
from app.db.database import session_maker
from app.db.models import CreditCard


def create_credit_cards(credit_cards):
    with session_maker() as session:
        try:
            session.add_all(credit_cards)
            session.commit()
            return Success(True)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_all_credit_cards(root):
    with session_maker() as session:
        return session.query(CreditCard).all()
