
import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

#authentication = Table(
#    'authentication',
#    metadata,
#    Column('id', Integer, primary_key=True),
#    Column('name', String(50)),
#)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('mail', String(100)),
    Column('password', String(150)),
    Column('token', String(150)),
    Column('token_exp', Integer),

)

database = Database(DATABASE_URI)