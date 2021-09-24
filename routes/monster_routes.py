from flask import Blueprint, jsonify, request
from ..osrs_box_direc import get_monster_by_name, all_monsters
from werkzeug.exceptions import BadRequestKeyError
monster_routes = Blueprint('monster_routes',__name__)

@monster_routes.route('/monster')
def get_monsters():
    try:
        name = request.args['name']
        monsters = get_monster_by_name(name)
        return jsonify(monsters)
    except BadRequestKeyError:
        return jsonify(get_monster_by_name('dragon'))
