#!/usr/bin/env python
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete."

@app.route('/restaurants/<int:restaurant_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to create a new menu item. Task 2 complete."

@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to create a new menu item. Task 3 complete."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)