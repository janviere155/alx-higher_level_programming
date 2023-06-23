#!/usr/bin/python3
"""Add a new state to the database"""
# Importing required modules/classes
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating a MySQL Engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    )

    # Binding MetaData with the Engine
    Base.metadata.create_all(engine)

    # Creating a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adding State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Printing ID of the newly added State
    print(new_state.id)
