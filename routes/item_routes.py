from flask import Blueprint, jsonify, request
from ..osrs_box_direc import get_item_by_name
from werkzeug.exceptions import BadRequestKeyError
item_routes = Blueprint('item_routes',__name__)

@item_routes.route('/hello')
def world():
    return jsonify({'msg': "hello, world"})

@item_routes.route("/item")
def get_item():
    try:
        name = request.args['name']
        items = get_item_by_name(name)
        return jsonify(items)
    except BadRequestKeyError:
        return jsonify(get_item_by_name(''))