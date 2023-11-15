from flask import Flask, jsonify, request, redirect
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address

from gen_data.gen_images import gen_identicon

from api_routes import api


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://",
)
app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({'message': 'You have exceeded the maximum request rate of 10 requests per minute, Sorry', 'status': 429}), 429

@app.route('/')
@limiter.exempt
def index():
    return jsonify({'message': 'Poof', 'status': 200}), 200

@app.route('/info')
@limiter.exempt
def info():
    return jsonify({'title': 'About The API','message':"This is an API that generetes fake/dummy data for frontend developers to test their app", 'status': 200}), 200


@app.route('/docs')
def redirect_docs():
    return redirect("https://imkowalski.github.io/PoofData/", code=302)