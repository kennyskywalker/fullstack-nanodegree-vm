from flask import Flask
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_creation import Base, Categories, LatestItems
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

engine = create_engine('sqlite:///catalogApp.db')

sessionDB = sessionmaker()
sessionDB.configure(bind=engine)
Base.metadata.create_all(engine)
session = sessionDB()

@app.route('/')
def categories():
    categories = session.query(Categories).filter_by(categories.id)
    print(categories)
        
    
@app.route('/catalog/items/')
def items():
    return 'Items from site'

@app.route('/catalog/new/')
def add_item():
    return 'Add item'

