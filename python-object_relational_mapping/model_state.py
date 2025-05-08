#!/usr/bin/python3
"""
Defines the State model and the Base for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

