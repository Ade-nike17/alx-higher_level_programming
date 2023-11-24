#!/usr/bin/python3

"""
This script prints the State object with the name passed as argument
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

    # Query to fetch State objects
    state = session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print('Not found')
    else:
        print("{0}".format(state.id))

    session.close()
