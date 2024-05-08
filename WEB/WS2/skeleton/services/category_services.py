from data.models import Category
from data.database import insert_query,read_query,query_count,update_query

def get_all(country_code=None):
    sql = '''SELECT * FROM categories'''

    if country_code:
        sql += f"country_code like '%{country_code}%'"

    return (Category.from_query_result(*row) for row in read_query(sql))


