#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    rlist = []

    bakeries = Bakery.query.all()

    for bakery in bakeries:
        rlist.append(bakery.to_dict())

    return rlist
@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    rlist = []

    exact_bakery = Bakery.query.filter_by(id=id).first()

    rlist.append(exact_bakery.to_dict())
    return rlist

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    # this is a query that takes all the baked goods in orders them by price highest to lowest
    rlist = [baked_good.to_dict() for baked_good in baked_goods]
    # this is a simpler way of writing a for loop and appending it to a list, here we just
    # do it all on one line
    return rlist
    

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).first()
    # just copied the logic above but did .first which grabs the first one ie the most expensive
    rlist = [baked_goods.to_dict()]
    # all we have to do is create a list with that one baked good

    return rlist

if __name__ == '__main__':
    app.run(port=5555, debug=True)
