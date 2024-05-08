from fastapi import APIRouter, Query, Response
from fastapi.responses import JSONResponse
from services import profiles_services
from data.models import Profile


profiles_router = APIRouter(prefix='/profiles')


@profiles_router.get('/')
def get_profiles(country_code: str | None = None):
    return profiles_services.get_all(country_code)


@profiles_router.get('/country_codes')
def get_country_codes():
    return profiles_services.get_all_country_codes()


@profiles_router.get('/{id}')
def get_by_id(id: int):
    profile = profiles_services.get_by_id(id)

    return profile or Response(status_code=404)


@profiles_router.get('/{id}/{product_id}')
def view_products_by_id(id:int, product_id: int):
    prod = profiles_services.view_product(id, product_id)

    return prod or Response(status_code=404)


@profiles_router.get('/get_ad/{ip_address}')
def get_ads(ip_address):
    ad = profiles_services.serve_ad(ip_address)

    return ad or Response(status_code=404)