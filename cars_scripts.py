# import sqlite3
# connection = None
from pony.orm import *
from pony.orm.core import sql_logger
from datetime import datetime
from random import randint
from creds import *
from creds.creds import LOGIN, PASSWORD, DB_NAME, DB_HOST

mysql = dict(provider = 'mysql',
             host = DB_HOST,
             port= 3306,
             user   = LOGIN,
             password = PASSWORD,
             db = DB_NAME
             )

sqlite = dict(
            provider = 'sqlite',
            filename = 'person.db',
            create_db = True
            )


db = Database()

# class Person(db.Entity):
#     name = Required (str)
#     age = Optional (int)
#     cars = Set ('Car') #Set - represents a collection, used for ‘to-many’ relationships

class Cars (db.Entity):
    my_id = Optional(int)
    car_name = Optional(str)
    car_brand = Optional(str)
    seats_num = Optional(int)
    manufacture_date = Optional(datetime)

class Cars_specs(db.Entity):
    car_ID=Optional(int)
    engine_size=Optional(int)
    color=Optional(str)
    wheels_size=Optional(int)
    safety_rating=Optional(int)


db.bind(mysql)
db.generate_mapping(create_tables=True)
set_sql_debug(True)
@db_session

def generate_unique_id():
    num = 1000

    def increment_id():
        nonlocal num
        current_id = num
        num += 1
        return current_id

    return int(increment_id())

# Створення екземпляру функції для генерації унікального числа
generate_id = generate_unique_id()

@db_session
def add_car():
    # p1 = Cars(my_id=1, car_name='740', car_brand="Volvo",seats_num = 2, manufacture_date = datetime(1990, 1, 1))
    # p2 = Cars(car_name='940', car_brand="Volvo",seats_num = 4, manufacture_date = datetime(1991, 1, 1))
    p3 = Cars(
        my_id = generate_unique_id(),
        car_name='240',
        car_brand="Nissan",
        seats_num = 6,
        manufacture_date = datetime(1966, 1, 1)
    )


@db_session
def add_car_specs():



# {'car_name': u'',
#  'cart_items': [1, 2],
#  'country': u'USA',
#  'email': u'john@example.com',
#  'id': 1,
#  'name': u'John Smith',
#  'orders': [1, 2],
#  'password': u'***'}

    db.commit()

@db_session
def output():
    print(Cars.select().show())

if __name__ == '__main__':
    add_car()
    output()

