#!/usr/bin/python3
"""Script to query the database and find the ID of a State by its name.
Usage: python script.py <mysql_username> <mysql_password> <database_name>
<state_name>"""

import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> "
              "<database_name> <state_name>")
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

    found = False
    for state in session.query(State).order_by(State.id):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            found = True
            break

    if not found:
        print("Not found")
