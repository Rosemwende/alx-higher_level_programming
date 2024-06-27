#!/usr/bin/python3
"""
Write a python file that contains the class definition of
a State and an instance Base = declarative_base()

"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
            import sys
            from sqlalchemy.orm import sessionmaker

            username = sys.argv[1]
            password = sys.argv[2]
            database = sys.argv[3]

            engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)

            iiase.metadata.create_all(engine)
