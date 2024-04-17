from fastapi import APIRouter
from services import projects_service
from common.responses import NotFound
from data.models import Project


project_router = APIRouter(prefix='/projects')


@project_router.get('/')
def get_projects(search=None):
    result = projects_service.all(search)

    return result


@project_router.get('/{id}')
def get_project_by_id(id: int):
    project = projects_service.get_by_id(id)

    if project is None:
        return NotFound()
    else:
        return project


@project_router.post('/', status_code=201)
def create_project(project: Project):
    return projects_service.create(project)