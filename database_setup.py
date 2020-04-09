from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

datetime.datetime.now()


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    solution = Column(String(42), nullable=False)
    guess = Column(String(42))
    timestamp = Column(TIMESTAMP, default=datetime.datetime.now())


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
