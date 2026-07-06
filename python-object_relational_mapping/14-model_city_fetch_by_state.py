#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Connect to MySQL and print all cities with their state name."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = {s.id: s.name for s in session.query(State).all()}
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(
            states[city.state_id], city.id, city.name))

    session.close()
