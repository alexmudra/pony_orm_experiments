# import sqlite3
# connection = None
from pony.orm import *
from pony.orm.core import sql_logger


mysql = dict(provider = 'mysql',
             host = 'mysql.freehostia.com',
             port= 3306,
             user   = 'alnik5_ei', #Пользователь: alnik5_ei@10.123.0.54
             password = 'sT#25&sf',
             db = 'alnik5_ei'
             )

sqlite = dict(
            provider = 'sqlite',
            filename = 'person.db',
            create_db = True
            )


db = Database()

class Person(db.Entity):
    name = Required (str)
    age = Optional (int)
    cars = Set ('Car') #Set - represents a collection, used for ‘to-many’ relationships

class Car (db.Entity):
    make = Required(str)
    model = Optional(str)
    owner = Required(Person)


# db.bind(provider='mysql', user='alnik5_ei', password='sT#25&sf', host='mysql.freehostia.com', database='alnik5_ei')


db.bind(mysql)
db.generate_mapping(create_tables=True)
set_sql_debug(True)
@db_session
def add_user():
    p1 = Person(name="One", age=45)
    c1 = Car(make="volvo", model='740', owner=p1)
    db.commit()

@db_session
def output():
    print(Person.select().show())

if __name__ == '__main__':
    add_user()
    output()


# class DB_one():
#
#     def __init__(self, filename) -> None:
#         self.conn_to_db(filename)
#
#     def conn_to_db(self, filename):
#         self.connection = sqlite3.connect(filename) # ':memory:'
#         self.cur = self.connection.cursor()
#
#
# cur = DB_one("lesson_19.db")
#
#
# def conn_to_db():
#     global connection
#     connection = sqlite3.connect(':memory:')
#     cur = connection.cursor()
#     return cur
#
#
# def create_table(cur, name="users"):
#     cur.execute(f'''CREATE TABLE IF NOT EXISTS {name}
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         last_name,
#         gender  INTGER,
#         hobbies,
#         street,
#         area,
#         landmark,
#         province,
#         city,
#         zip
#         );''')
#     connection.commit()
#
#
# def insert_data(cur, csv):
#     cur.execute(f"INSERT INTO users (first_name, last_name) VALUES {csv}")
#     connection.commit()
#
#
# def select_data(cur, select):
#     return cur.execute(select).fetchall()
#
#
# cur = conn_to_db()
#
# create_table(cur)
#
# csv = "('David', 'Solomonovich')"
# csv2 = "('Ivan', 'Pobivan')"
# insert_data(cur, csv)
# insert_data(cur, csv2)
# data = select_data(cur, 'SELECT * FROM users;')
# print(data)
#
# connection.close()
# # .fetchmany(3) - три перші результати, далі наступні