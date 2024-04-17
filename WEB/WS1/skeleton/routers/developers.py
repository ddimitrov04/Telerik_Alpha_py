from fastapi import APIRouter
from services import developer_service
from common.responses import NotFound
from data.models import Developer

developer_router = APIRouter(prefix='/developers')


@developer_router.get('/')
def get_projects(search=None):
    result = developer_service.all(search)

    return result


@developer_router.get('/{id}')
def get_project_by_id(id: int):
    project = developer_service.get_by_id(id)

    if project is None:
        return NotFound()
    else:
        return project


@developer_router.post('/', status_code=201)
def create_project(developer: Developer):
    return developer_service.create(developer)