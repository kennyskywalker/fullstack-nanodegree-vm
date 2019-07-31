from flask import Flask, url_for
from flask import redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_creation import Base, Categories, LatestItems
from flask import Flask, render_template

app = Flask(__name__)

engine = create_engine('sqlite:///catalogApp.db')

sessionDB = sessionmaker()
sessionDB.configure(bind=engine)
Base.metadata.create_all(engine)
session = sessionDB()

@app.route('/')
@app.route('/categories/<int:categories_id>/')
def index(categories_id):
    categories = session.query(Categories).all(categories_id)
    items = session.query(LatestItems).filter_by(categories_id=categories.id)
    return render_template('index.html', categories=categories, items=items)

