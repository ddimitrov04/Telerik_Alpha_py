from data.models import Developer
from data.database import insert_query, read_query, update_query

def all(search: str = None):
    if search is None:
        data = read_query(
            '''SELECT id, name, level FROM devs'''
        )
    else:
        data = read_query(
            '''SELECT id, name, level FROM devs
            WHERE name LIKE ?''', (f'%{search}%',)
        )

    return (Developer.from_query_result(*row) for row in data)

def get_by_id(id: int):
    data = read_query('''SELECT id, name, level
            FROM devs WHERE id = ?''', (id,))

    return next((Developer.from_query_result(*row) for row in data), None)


def create(developer: Developer):
    generated_id = insert_query(
        'INSERT INTO devs(name, level) VALUES(?,?)',
        (developer.name, developer.level))

    developer.id = generated_id
    return developer