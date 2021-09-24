from flask import Blueprint, jsonify, request
from ..osrs_box_direc import get_prayer_by_name
from werkzeug.exceptions import BadRequestKeyError
prayer_routes = Blueprint('prayer_routes',__name__)


@prayer_routes.route("/prayer")
def get_item():
    try:
        name = request.args['name']
        prayers = get_prayer_by_name(name)
        return jsonify(prayers)
    except BadRequestKeyError:
        return jsonify(get_prayer_by_name(''))