# app/routes.py

from flask import Blueprint, jsonify, request
from .models import Item
from .extensions import db

item_routes = Blueprint('items', __name__)

@item_routes.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@item_routes.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201
