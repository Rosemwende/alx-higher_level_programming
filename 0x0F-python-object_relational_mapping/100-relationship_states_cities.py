#!/usr/bin/python3
"""
script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        california = State(name="California")
        session.add(california)
        session.commit()

        san_francisco = City(name="San Francisco", state=california)
        session.add(san_francisco)
        session.commit()

        print(san_francisco.id)

        session.close()
