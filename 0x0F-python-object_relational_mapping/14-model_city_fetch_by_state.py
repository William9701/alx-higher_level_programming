#!/usr/bin/python3
"""joins two table to provide a combined output"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

port = 3306
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        sys.argv[1],
        sys.argv[2],
        port,
        sys.argv[3]
        ),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name). \
                filter_by(id=city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))

        session.close()
