#!/usr/bin/python3
"""
Script to delete objects from the database based on a condition.
Usage: python script.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> "
            "<database_name>")
        sys.exit(1)

    # Create the SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)

    # Bind the Base class to the engine
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Iterate over states and delete those with 'a' in their name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            session.delete(state)

    # Commit the transaction to save the changes
    session.commit()
