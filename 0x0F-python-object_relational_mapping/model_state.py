#!/usr/bin/python3
""" Contains `state` class and `Base`, an instance of declarative_base()"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    State class:
        id - autogenerated INT
        name - name of the state STRING
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
