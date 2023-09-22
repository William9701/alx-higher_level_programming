#!/usr/bin/python3
"""This script defines a SQLAlchemy model class for a 'cities' table."""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


# Establish a connection to the MySQL database


class City(Base):
    """A SQLAlchemy model representing a city in the 'cities' table."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
