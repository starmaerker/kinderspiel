import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    solution = Column(Integer, nullable=False)
    guess = Column(String(42))
    timestamp = Column(TIMESTAMP, default=datetime.datetime.now())


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)