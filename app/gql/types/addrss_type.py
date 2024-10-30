from graphene import ObjectType, Int, String


class AddressType(ObjectType):
    id = Int()
    state = String()
    city = String()
    street = String()
    street_number = Int()
    user_id = Int()
