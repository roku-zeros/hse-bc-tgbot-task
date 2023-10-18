from pony.orm import *
from datetime import datetime

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Optional(str)
    last_action_date = Optional(datetime)


db.bind(provider='sqlite', filename='users.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
