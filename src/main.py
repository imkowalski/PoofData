from flask import Flask, jsonify, request
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address

from gen_data.gen_images import gen_identicon

from api_routes import api


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1000 per hour"],
    storage_uri="memory://",
)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
@limiter.exempt
def index():
    return jsonify({'message': 'Poof', 'status': 200})

@app.route('/info')
@limiter.exempt
def info():
    return jsonify({'title': 'About The API','message':"asd", 'status': 200})


