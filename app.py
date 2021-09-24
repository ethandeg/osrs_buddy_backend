from flask import Flask, jsonify, request
from .routes import item_routes, monster_routes, prayer_routes

app = Flask(__name__)
app.debug = True
BASE_URL = '/api/v1'
app.register_blueprint(item_routes, url_prefix=f'{BASE_URL}/items')
app.register_blueprint(monster_routes, url_prefix=f'{BASE_URL}/monsters')
app.register_blueprint(prayer_routes, url_prefix=f'{BASE_URL}/prayers')


@app.route(BASE_URL)
def say_hello():
    return jsonify({'msg': 'hello, worlds'})


