#!/usr/bin/python3
"""Delete a state in the database with letter a"""
# Import necessary libraries
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Define database credentials
    username = argv[1]
    password = argv[2]
    dbase_name = argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbase_name}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    # Create session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects with a name containing the letter "a"
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()

    # Close session
    session.close()
