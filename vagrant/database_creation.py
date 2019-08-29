import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class LatestItems(Base):
    __tablename__ = 'latest_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    categories_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories, backref=backref('category', uselist=True))


engine = create_engine('sqlite:///catalogApp.db')

Base.metadata.create_all(engine)