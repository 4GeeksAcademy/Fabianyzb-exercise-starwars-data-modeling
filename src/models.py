import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    charId = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_date = Column(String(250))
    height = Column(Integer, primary_key=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planetId = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer, primary_key=False)
    diameter = Column(Integer, primary_key=False)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrin = Column(String(250))


class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    shipId = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    max_speed = Column(Integer, primary_key=False)
    passengers = Column(Integer, primary_key=False)
    starship_class = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    favId = Column(Integer, primary_key=True)
    charId = Column(Integer, ForeignKey('characters.id'))
    planetId = Column(Integer, ForeignKey('planets.id'))
    shipId = Column(Integer, ForeignKey('ships.id'))
    user = Column(Integer, ForeignKey('user.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


# person_id = Column(Integer, ForeignKey('person.id'))