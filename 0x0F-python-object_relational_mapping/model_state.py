#!/usr/bin/python3
"""creates a table states"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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

class State(Base):
	__tablename__ = 'states'

	id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	name = Column(String(128), nullable=False)

cursor.close()