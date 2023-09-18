#!/usr/bin/python3
<<<<<<< HEAD
"""Module that retrieves and prints all\
        states from a MySQL database using SQLAlchemy."""
=======
"""Start link class to table in database"""
>>>>>>> 3aba1fb371494ca1cb13fc9f4f7dfccf46b6453e

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()

    # Retrieve all states from the database and print their IDs and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
