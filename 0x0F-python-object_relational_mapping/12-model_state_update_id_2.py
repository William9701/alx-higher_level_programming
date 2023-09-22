#!/usr/bin/python3
"""
Script to update data in the database.
Usage: python script.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from model_state import Base, State
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

    # Retrieve the State object with id=2 and update its name
    update = session.query(State).filter_by(id=2).first()
    if update:
        update.name = "New Mexico"

    # Commit the transaction to save the changes
    session.commit()
