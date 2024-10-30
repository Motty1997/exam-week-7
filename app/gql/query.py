from graphene import ObjectType, List
from app.gql.types.addrss_type import AddressType
from app.gql.types.credit_card_type import CreditCardType
from app.gql.types.user_type import UserType
from app.repository.address_rpository import get_all_addresses
from app.repository.credit_card_repository import get_all_credit_cards
from app.repository.user_repository import get_all_users


class Query(ObjectType):
    users = List(UserType)
    addresses = List(AddressType)
    credit_cards = List(CreditCardType)

    @staticmethod
    def resolve_users(root, info):
        return get_all_users(root)

    @staticmethod
    def resolve_address(root, info):
        return get_all_addresses(root)

    @staticmethod
    def resolve_credit_cards(root, info):
        return get_all_credit_cards(root)
