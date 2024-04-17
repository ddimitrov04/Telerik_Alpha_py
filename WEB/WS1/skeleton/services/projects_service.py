from data.models import Project
from data.database import insert_query, read_query, update_query


def all(search: str = None):
    if search is None:
        data = read_query(
            '''SELECT id, name, status, team_limit FROM projects'''
        )
    else:
        data = read_query(
            '''SELECT id, name, status, team_limit FROM projects
            WHERE name LIKE ?''', (f'%{search}%',)
        )

    return (Project.from_query_result(*row) for row in data)

def get_by_id(id: int):
    data = read_query('''SELECT id, name, status, team_limit 
            FROM projects WHERE id = ?''', (id,))

    return next((Project.from_query_result(*row) for row in data), None)

def create(project: Project):
    generated_id = insert_query(
        'INSERT INTO projects(name, status, team_limit) VALUES(?,?,?)',
        (project.name, project.status, project.team_limit))

    project.id = generated_id
    return project