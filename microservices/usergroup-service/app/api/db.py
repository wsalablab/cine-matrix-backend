
import os

from sqlalchemy import (Column, ForeignKey, Integer, MetaData, PrimaryKeyConstraint, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

usergroup = Table(
    'usergroup',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

group = Table(
    'group',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

user_group = Table(
    'user_group',
    metadata,
    Column('id_user', Integer, nullable=False),
    Column('id_group', Integer, ForeignKey('group.id'), nullable=False),
    PrimaryKeyConstraint('id_user', 'id_group')
)

database = Database(DATABASE_URI)