#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine and connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states where the name contains 'a', ordered by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

