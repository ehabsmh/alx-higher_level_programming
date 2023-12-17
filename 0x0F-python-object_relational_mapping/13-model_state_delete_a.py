#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_uri.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    states_with_a = session.query(State).filter(
        State.name.like("%a%"))

    for state in states_with_a:
        session.delete(state)

    session.commit()
