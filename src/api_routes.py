from flask import Blueprint, jsonify, request,send_file
from gen_data import gen_images
api = Blueprint('api', __name__)

@api.route('/')
def index():
    return jsonify({'message': "I'm the Poof API", 'status': 200})


@api.route('/gen_identicon/<int:id>')
def gen_identicon(id):
    if request.args.get('size'):
        size = int(request.args.get('size'))
        image = gen_images.gen_identicon(id,size=size)
    else:
        image = gen_images.gen_identicon(id)
    if image is None:
        return jsonify({'message': 'Image size too large', 'status': 400})
    return send_file(image, mimetype='image/png')