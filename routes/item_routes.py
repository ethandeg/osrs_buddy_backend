from flask import Blueprint, jsonify, request
from ..osrs_box_direc import get_item_by_name
item_routes = Blueprint('item_routes',__name__)

@item_routes.route('/hello')
def world():
    return jsonify({'msg': "hello, world"})

@item_routes.route("/item")
def get_item():
    print(request.args)
    name = request.args['name']
    something = get_item_by_name(name)
    return jsonify(something)