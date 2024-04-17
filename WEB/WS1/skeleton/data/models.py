from pydantic import BaseModel
from typing import List, Optional


class Developer(BaseModel):
    id: int
    name: str
    level: str

    @classmethod
    def from_query_result(cls, id, name, level):
        return cls(
            id=id,
            name=name,
            level=level
        )


class Project(BaseModel):
    id: int
    name: str
    status: str
    team_limit: int

    @classmethod
    def from_query_result(cls, id, name, status, team_limit):
        return cls(
            id=id,
            name=name,
            status=status,
            team_limit=team_limit
        )

class DeveloperProject(BaseModel):
    developer_id: int
    project_id: int


class DeveloperWithProjects(Developer):
    projects: Optional[List[Project]] = []


class ProjectWithDevelopers(Project):
    developers: Optional[List[Developer]] = []