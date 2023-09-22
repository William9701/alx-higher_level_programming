#!/usr/bin/python3
"""This module connects to a MySQL database and prints all states from the
'states' table."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def engine_form(user, psd, db):
    """ create an engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user,
                                                         psd,
                                                         db),
        pool_pre_ping=True)

    Base.metadata.bind = engine

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and print their ids and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine_form(username, password, database)


# Create an SQLAlchemy engine for connecting to the database
