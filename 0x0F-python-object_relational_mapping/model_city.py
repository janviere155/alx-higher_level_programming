#!/usr/bin/python3
"""Contains the `City` class and `Base`, an instance of declarative_base()"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


class City(Base):
    """City class:
    id - identification auto-generated not null
    name - name of the city in the database
    state_id - refers to the id in the states table
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
