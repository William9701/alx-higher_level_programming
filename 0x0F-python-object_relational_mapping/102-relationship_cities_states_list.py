#!/usr/bin/python3
"""
Script that lists all State objects and their corresponding City objects from
the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> "
            "<database_name>")
        sys.exit(1)

    # Create the SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]),
        pool_pre_ping=True)

    # Bind the Base classes to the engine
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the City objects and access the linked State objects via the
    # state relationship
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

