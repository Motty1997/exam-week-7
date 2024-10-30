from graphene import ObjectType, Int, String, Date


class CreditCardType(ObjectType):
    id = Int()
    card_number = String()
    cvv = Int()
    expiration = Date()
    identifier = String()
    user_id = Int()
