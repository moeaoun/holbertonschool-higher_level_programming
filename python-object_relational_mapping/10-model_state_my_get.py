#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Parse command-line arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Create SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state using parameter binding (SQL injection safe)
    result = session.query(State).filter(State.name == state_name).first()

    # Output result
    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()

