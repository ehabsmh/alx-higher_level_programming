#!/usr/bin/python3
"""Lists all cities objects"""

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_uri.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    results = session.query(City.id, City.name).join(
        State).order_by(City.id).add_columns(State.name)

    for row in results:
        print(f"{row[2]}: ({row[0]}) {row[1]}")
