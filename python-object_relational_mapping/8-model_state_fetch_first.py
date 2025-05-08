#!/usr/bin/python3
"""
Lists the first State object from the database hbtn_0e_6_usa using SQLAlchemy.
If the table is empty, print 'Nothing'
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

    # Query the first state, ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if the state exists and display it
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

