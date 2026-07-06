#!/usr/bin/python3
"""Prints the State object with a given name from hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Connect to MySQL and print the state matching the given name."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        func.binary(State.name) == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
