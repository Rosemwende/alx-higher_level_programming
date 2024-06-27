#!/usr/bin/python3
"""
write a script 14-model_city_fetch_by_state.py
that prints all City objects from the
database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>")
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(State.name, City.id, City.name).join(City).order_by(City.id).all()

        for state_name, city_id, city_name in cities:
            print(f"{state_name}: ({city_id}) {city_name}")

            session.close()
