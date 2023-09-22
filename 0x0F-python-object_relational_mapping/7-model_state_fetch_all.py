#!/usr/bin/python3
"""This module connects to a MySQL database and prints all states from the
'states' table."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an SQLAlchemy engine for connecting to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.bind = engine

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and print their ids and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
