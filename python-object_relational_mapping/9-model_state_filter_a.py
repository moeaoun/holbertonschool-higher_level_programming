#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{mysql_db}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a' in their name, sorted by states.id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

