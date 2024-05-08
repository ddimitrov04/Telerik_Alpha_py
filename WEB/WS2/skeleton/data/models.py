from pydantic import BaseModel, constr, confloat, conint


class Profile(BaseModel):
    id: int | None
    ip_address: constr(min_length=1)
    country_code: constr(min_length=1)
    favourite_categories: list = []

    @classmethod
    def from_query_result(cls, id, ip_address, country_code, favourite_categories=None):
        return cls(
            id=id,
            ip_address=ip_address,
            country_code=country_code,
            favourite_categories=favourite_categories or []
        )


class Category(BaseModel):
    id: int
    name: constr(min_length=1)
    relevance: int


    @classmethod
    def from_query_result(cls, id, name, relevance):
        return cls(
            id=id,
            name=name,
            relevance=relevance
        )


class Interest(BaseModel):
    profile_id: int
    category_id: int
    relevance: conint(ge=1)

    @classmethod
    def from_query_result(cls, relevance):
        return cls(
            relevance=relevance)


class Product(BaseModel):
    id: int | None
    name: constr(min_length=1)
    price: confloat(gt=0.01, lt=100000000)
    category_id: int

    @classmethod
    def from_query_result(cls, id, name, price, category_id):
        return cls(
            id=id,
            name=name,
            price=price,
            category_id=category_id
        )