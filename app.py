from flask import Flask, jsonify, request
from osrsbox_api import item, get_item_by_name

app = Flask(__name__)


@app.route("/")
def say_hello():
    return jsonify(item)


@app.route("/items")
def get_item():
    name = request.args['name']
    item = get_item_by_name(name)
    return jsonify(item)