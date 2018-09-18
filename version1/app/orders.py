from flask import Flask, request
from flask_restful import Resource
from .models import Order, orders
class DisplayOrders(Resource):
    def get(self):
        return {"orders":[order.successive() for order in orders]}

    def post(self):
        data = request.get_json()
        order = Order(data['name'], data["price"],data['description'])
        orders.append(order)

        return {"message":"Food order created"}, 201