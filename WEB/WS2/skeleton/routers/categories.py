from fastapi import APIRouter, Query, Response
from fastapi.responses import JSONResponse
from services import category_services
from data.models import Category


categories_router = APIRouter(prefix='/categories')


@categories_router.get('/')
def get_categories(country_code: str | None = None):
    return category_services.get_all(country_code)

