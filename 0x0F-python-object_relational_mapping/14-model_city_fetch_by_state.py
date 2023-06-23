#!/usr/bin/python3
"""print all cities based on the state"""
from sys import argv

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print(f"{city[0]}: ({str(city[1])}) {city[2]}")
