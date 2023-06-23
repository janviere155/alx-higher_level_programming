#!/usr/bin/python3
"""get a state specified in database"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connecting to the Database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    )

    Base.metadata.create_all(engine)
    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the Database
    states = session.query(State).filter(State.name == argv[4]).all()

    # Checking if State is Not Found
    if len(states) == 0:
        print("Not found")

    # if State is Found
    else:
        for state in states:
            print(state.id)
