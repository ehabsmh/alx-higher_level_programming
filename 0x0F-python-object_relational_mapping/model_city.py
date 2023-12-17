#!/usr/bin/python3
"""Contains the class definition of a City"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines the table `cities`"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
