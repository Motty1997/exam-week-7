from datetime import date
from returns.result import Failure
from app.db.database import engin
from app.db.models import UserDetails, Base, Address, CreditCard
from app.repository.address_rpository import create_addresses
from app.repository.credit_card_repository import create_credit_cards
from app.repository.user_repository import create_users


users_data = [
        UserDetails(
        first_name="mordechaim",
        last_name="shteren",
        email="mordechaim@gmail.shteren",
        user_type="regular",
        identifier="111111111",
        ),
        UserDetails(
        first_name="chaim",
        last_name="ren",
        email="chaim@gmail.ren",
        user_type="regular",
        identifier="111111112",
        ),
        UserDetails(
        first_name="mordechai",
        last_name="shte",
        email="mordechai@gmail.shte",
        user_type="regular",
        identifier="111111113",
        )
    ]

addresses_data = [
        Address(
            state='Tel Aviv',
            city='Tel Aviv',
            street='Rothschild',
            street_number=15,
            user_id=1
        ),Address(
            state='Jerusalem',
            city='Jerusalem',
            street='King David',
            street_number=10,
            user_id=2
        ),Address(
            state='Haifa',
            city='Haifa',
            street='Ben Gurion',
            street_number=5,
            user_id=3
        )]
credit_cards_data = [
        CreditCard(
        card_number='1234567812345678',
        cvv=123,
        expiration=date(2025, 12, 1),
        identifier='abc123',
        user_id=1
    ),
             CreditCard(
        card_number='8765432187654321',
        cvv=456,
        expiration=date(2026, 5, 1),
        identifier='def456',
        user_id=2
    ), CreditCard(
        card_number='1111222233334444',
        cvv=789,
        expiration=date(2027, 8, 1),
        identifier='ghi789',
        user_id=3)
    ]

def init_db():
    Base.metadata.drop_all(engin)
    Base.metadata.create_all(engin)
    res = create_users(users_data)
    res1 = create_addresses(addresses_data)
    res2 = create_credit_cards(credit_cards_data)
    if isinstance(res, Failure):
        raise Exception(res.failure())
    if isinstance(res1, Failure):
        raise Exception(res1.failure())
    if isinstance(res2, Failure):
        raise Exception(res2.failure())
