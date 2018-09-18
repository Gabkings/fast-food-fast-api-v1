from flask import Flask, request
from flask_restful import Resource
from .models import Order, orders
class DisplayOrders(Resource):
    def get(self):
        return {"orders":[order.successive() for order in orders]}

