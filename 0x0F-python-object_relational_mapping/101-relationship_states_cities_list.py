#!/usr/bin/python3
"""this module creates a city from the relationship with the state"""
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

    # Create the SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]),
        pool_pre_ping=True)

    # Bind the Base classes to the engine
    Base.metadata.bind = engine

    # Create the 'states' and 'cities' tables (if not already created)
    Base.metadata.create_all(bind=engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    state_and_cities = session.query(State).order_by(State.id).all()

    for state in state_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.city:
            print("\t{}: {}".format(city.id, city.name))
