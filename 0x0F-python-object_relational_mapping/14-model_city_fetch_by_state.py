#!/usr/bin/python3
"""
Script to join two tables and provide a combined output.
Usage: python script.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> "
            "<database_name>")
        sys.exit(1)

    # Define the port
    port = 3306

    # Create the SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(sys.argv[1], sys.argv[2],
                                                       port, sys.argv[3]),
        pool_pre_ping=True)

    # Bind the Base classes to the engine
    Base.metadata.bind = engine
    # Create the 'states' and 'cities' tables (if not already created)
    Base.metadata.create_all(bind=engine)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the combined information from both tables
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name).filter_by(
            id=city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
