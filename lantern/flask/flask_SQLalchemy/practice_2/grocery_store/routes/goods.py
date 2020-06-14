from flask import request
from flask_restful import Resource, marshal

from grocery_store.models import Good
from grocery_store.db import db
from grocery_store.routes.marshal_structure import goods_structure


class Goods(Resource):
    def get(self, good_id=None):
        if good_id:
            good = Good.query.get(good_id)
            if good:
                return marshal(good, goods_structure)
<<<<<<< HEAD
            return f"No such good with id: {good_id}"
        return marshal(Good.query.all(), goods_structure)

    def post(self):
        good = Good(**request.json)
        db.session.add(good)
        db.session.commit()
        return f"Successfully added a new good {good}"

    def put(self, good_id):
        good = Good.query.get(good_id)
        good.name = request.json.get("name", good.name)
        good.brand = request.json.get("brand", good.brand)
        good.price = request.json.get("price", good.price)
        db.session.commit()
        return f"Successfully updated Good with id: {good_id}"

    def delete(self, good_id):
        good = Good.query.get(good_id)
        db.session.delete(good)
        db.session.commit()
        return f"Successfully deleted User with id: {good_id}"
=======
            return f"No such store with id: {good_id}"
        return marshal(Good.query.all(), goods_structure)

    def post(self):
        temp_list_goods = request.json
        for item in temp_list_goods:
            temp = Good(**item)
            db.session.add(temp)
        db.session.commit()
        return f"Number of created items {len(temp_list_goods)}"

    def put(self):
        temp_list_goods = request.json
        for temp in temp_list_goods:
            item = Good.query.get(temp['good_id'])
            item.brand = temp['brand']
            item.name = temp['name']
            item.price = temp['price']
        db.session.commit()
        return f"Number of updated {len(temp_list_goods)}"

    def delete(self):
        temp_list_goods = request.json
        for temp in temp_list_goods:
            item = Good.query.get(temp['good_id'])
            db.session.delete(item)
        db.session.commit()
        return f"Number of deleted items: {len(temp_list_goods)}"
>>>>>>> SQLalchemy
