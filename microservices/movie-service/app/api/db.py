
import os

from sqlalchemy import (Column, ForeignKey, Integer, MetaData, PrimaryKeyConstraint, String, Table, UniqueConstraint,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies_tdmb',
    metadata,
    Column('id_tdmb', Integer, primary_key=True),
    Column('title', String(50)),
    Column('poster', String(1500)),
    Column('synopsis', String(1500)),
)

genre = Table(
    'genre',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

movie_genre = Table(
    'movie_genre',
    metadata,
    Column('id_movie', Integer, nullable=False),
    Column('id_genre', Integer, ForeignKey('genre.id'), nullable=False),
    PrimaryKeyConstraint('id_movie', 'id_genre')
)

appreciation = Table(
    'appreciation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    UniqueConstraint('name')
)

movie_watch = Table(
    'movie_watch',
    metadata,
    Column('id_user', Integer, nullable=False),
    Column('id_movie', Integer, ForeignKey('movies_tdmb.id_tdmb'), nullable=False),
    Column('id_appreciation', Integer, ForeignKey('appreciation.id'), nullable=False),
    PrimaryKeyConstraint('id_user', 'id_movie')
)

database = Database(DATABASE_URI)