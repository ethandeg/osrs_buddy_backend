from flask import Flask, jsonify, request
from .routes import item_routes

app = Flask(__name__)
app.debug = True
BASE_URL = '/api/v1'
app.register_blueprint(item_routes, url_prefix=f'{BASE_URL}/items')

@app.route(BASE_URL)
def say_hello():
    return jsonify({'msg': 'hello, worlds'})


