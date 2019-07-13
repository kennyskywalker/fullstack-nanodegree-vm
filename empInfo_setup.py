import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    jobID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    jobTitle = Column(String(250), nullable=False)
    reportManager = Column(String(250), nullable=False)
    jobLevel = Column(Integer, nullable=False)
    location = Column(String(250), nullable=False)

engine = create_engine('sqlite:///empInfo.db')

Base.metadata.create_all(engine)