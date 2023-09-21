#!/usr/bin/python3
"""This script defines a SQLAlchemy model class for a 'cities' table."""

from model_state import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# Establish a connection to the MySQL database

Base = declarative_base()


class City(Base):
    """A SQLAlchemy model representing a city in the 'cities' table."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


# Close the database cursor

