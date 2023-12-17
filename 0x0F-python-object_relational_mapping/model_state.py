#!/usr/bin/python3
"""Defines class `State` and an instance `Base = declarative_base()`"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the table `states`"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True,
                unique=True)

    name = Column(String(128), nullable=False)
