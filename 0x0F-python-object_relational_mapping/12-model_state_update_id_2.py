#!/usr/bin/python3
"""Update the state in the datatbase"""
# import the required modules
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create an engine to connect to the MySQL server
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    )

    Base.metadata.create_all(engine)
    # create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # get the state object where id=2
    state = session.query(State).filter_by(id=2).one()

    # change the name of the state object to 'New Mexico'
    state.name = "New Mexico"

    # commit the changes to the database
    session.commit()
