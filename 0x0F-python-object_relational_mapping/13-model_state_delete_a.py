#!/usr/bin/python3

"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                     argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to delete State object that contains 'a'
    state_a = session.query(State).filter(State.name.contains('a'))
    for state in state_a:
        session.delete(state)
    session.commit()
    session.close()
