#!/usr/bin/python3
"""Lists all State objects that contain the letter a"""

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

    state_id = session.query(State.id).filter(State.name == argv[4]).first()

    if not state_id:
        print("Not found")
    else:
        print(state_id[0])
