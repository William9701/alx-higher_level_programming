#!/usr/bin/python3
"""creates a table cities"""

from model_state import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import MySQLdb

db = MySQLdb.connect(
            host='localhost',
            user="root",
            port=3306,
            passwd="william667",
            db="hbtn_0e_6_usa"
        )
cursor = db.cursor()
Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),  nullable=False,)


cursor.close()
