#!/usr/bin/python3
""" changes the name of a State object from the database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import (create_engine)
from sqlalchemy import asc


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = select(State).where(State.id == 2)
    state = session.execute(query).fetchone().State
    state.name = 'New Mexico'
    session.commit()
    session.close()
