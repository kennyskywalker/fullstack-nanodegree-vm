#!/usr/bin/env python
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_creation import Base, Categories, LatestItems

app = Flask(__name__)
engine = create_engine('sqlite:///catalogApp.db')
Base.metadata.bind=engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/categories')
def categories():
    categories = session.query(Categories).all()
    latest_items = session.query(LatestItems).all()
    return render_template('categories.html', categories=categories, latest_items=latest_items, login=False)

@app.route('/latest_items')
def latest_items():
    latest_items = session.query(LatestItems).all()
    return render_template('latest_items.html', latest_items=latest_items, login=True)    


@app.route('/login')
def login():
    return render_template('login.html', login=False)

if __name__ == '__main__':
    app.secret_key =  'super_secret_key'   
    app.debug = True
    app.run(host='0.0.0.0', port=5000)