from data.models import Profile,Product
from data.database import insert_query,read_query,query_count,update_query
from data.models import Interest, Category
from fastapi import Response,HTTPException
from math import ceil
import random

def get_all(country_code=None):
    sql = 'SELECT id, ip_address, country_code FROM profiles'

    if country_code:
        sql += f" WHERE country_code like '%{country_code}%'"

    return (Profile.from_query_result(*row) for row in read_query(sql))


def get_all_country_codes():
    sql = '''SELECT DISTINCT country_code FROM profiles'''
    rows = read_query(sql)
    return [row[0] for row in rows]


def get_by_id(id: int):
    profile_raw = read_query('''SELECT id, ip_address, country_code FROM profiles WHERE id = ?''', (id,))

    if not profile_raw:
        return Response(status_code=404, content=f"No profile with that id")

    categories_sql = '''
                SELECT c.id, c.name, i.relevance FROM categories c JOIN interests i ON c.id = i.category_id 
                WHERE i.profile_id = ? ORDER BY i.relevance DESC
            '''

    categories_raw = read_query(categories_sql, (id,))

    return Profile.from_query_result(*profile_raw[0],[Category.from_query_result(*row) for row in categories_raw])


def view_product(profile_id:int, product_id:int):
    profile_raw = read_query('''SELECT id, ip_address, country_code FROM profiles WHERE id = ?''', (profile_id,))

    if not profile_raw:
        return Response(status_code=404, content=f"No profile with that id")


    products_raw = read_query('''SELECT p.id, p.name, p.price, p.category_id 
        FROM products p JOIN categories c on p.category_id = c.id WHERE p.id = ?''',(product_id,))

    if not products_raw:
        return Response(status_code=404, content=f"No product with that id")

    category_id_sql = "SELECT category_id FROM products WHERE id = ?"
    category_id = read_query(category_id_sql, (product_id,))[0][0]

    interest_sql = 'SELECT relevance FROM interests WHERE profile_id = ? AND category_id = ?'
    existing_relevance = read_query(interest_sql, (profile_id, category_id))

    if existing_relevance:
        new_relevance = existing_relevance[0][0]*1.05
        update_query('UPDATE interests SET relevance = ? WHERE profile_id = ? AND category_id = ?',(ceil(new_relevance), profile_id, category_id))
    else:
        insert_query('INSERT INTO interests (profile_id, category_id, relevance) VALUES (?, ?, 1)', (profile_id, category_id))

    return (Product.from_query_result(*row) for row in products_raw)



def serve_ad(ip_address):
    interests_raw = read_query('''SELECT category_id FROM interests 
    JOIN profiles ON interests.profile_id = profiles.id
    WHERE ip_address = ?''', (ip_address,))

    if interests_raw:
        top_interests_sql = '''
            SELECT category_id 
            FROM interests 
            JOIN profiles ON interests.profile_id = profiles.id 
            WHERE ip_address = ? 
            ORDER BY interests.relevance DESC 
            LIMIT 3
        '''
        top_interests = [row[0] for row in read_query(top_interests_sql, (ip_address,))]

        product_sql = '''SELECT id, name, price FROM products WHERE category_id IN ({})
         ORDER BY RANDOM() LIMIT 1'''.format(', '.join('?' * len(top_interests)))

        product = read_query(product_sql, top_interests)
    else:
        product_sql = 'SELECT id, name, price FROM products ORDER BY RANDOM() LIMIT 1'
        product = read_query(product_sql)

    return Product.from_query_result(*product)



# profile_raw = read_query('''SELECT id, ip_address, country_code FROM profiles WHERE id = ?''', (id,))
#
#     if not profile_raw:
#         return Response(status_code=404, content=f"No profile with that id")
#
#     categories_sql = '''
#                 SELECT c.id, c.name, i.relevance FROM categories c JOIN interests i ON c.id = i.category_id
#                 WHERE i.profile_id = ?
#             '''
#
#     categories_raw = read_query(categories_sql, (id,))
#
#     products_raw = read_query('''SELECT p.id, p.name, p.price, p.category_id
#     FROM products p JOIN categories c on p.category_id = c.id ''')
#
#     return Profile.from_query_result(*profile_raw[0],[Category.from_query_result(*row, [Product.from_query_result(*jin) for jin in products_raw]) for row in categories_raw])