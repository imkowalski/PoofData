from flask import Blueprint, jsonify, request,send_file
from gen_data import gen_images, gen_text, gen_obj, gen_bulk
import time,random

api = Blueprint('api', __name__)
@api.route('/')
def index():
    return jsonify({'message': "I'm the Poof API", 'status': 200})



@api.route('/image/gen_identicon/<int:id>')
def gen_identicon(id):
    if request.args.get('size'):
        size = int(request.args.get('size'))
        image = gen_images.gen_identicon(id,size=size)
    else:
        image = gen_images.gen_identicon(id)
    if image is None:
        return jsonify({'message': 'Image size too large', 'status': 400})
    return send_file(image, mimetype='image/png')

@api.route('/image/gen_image')
def gen_image():
    if request.args.get('width') and request.args.get('height'):
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))
        image = gen_images.gen_image(width,height)
    else:
        return jsonify({'message': 'Please provide width and height', 'status': 400})
    return send_file(image, mimetype='image/png')

@api.route('/user/profile')
def gen_profile():
    seed = int(str(time.time())[-6:])+random.randint(-10000,10000)
    args = request.args
    if args.get('seed'):
        seed = int(request.args.get('seed'))
    
    res = {}
    for i in args.keys():
        if i == "seed":
            continue;
        if i == "name":
            res["name"] = gen_text.gen_name(seed)[0]+" "+gen_text.gen_name(seed)[1]
        if i == "email":
            res["email"] = gen_text.gen_email(seed,gen_text.gen_name(seed)[0])
        if i == "phone":
            res["phone"] = gen_text.gen_phone(seed)
        if i == "job":
            res["job"] = gen_text.gen_job(seed)
        if i == "id":
            res["id"] = seed
    if res == {}:
        res = gen_text.gen_profile(seed)
    return jsonify(res)


@api.route('/object/post')
def gen_post():
    seed = time.time()
    if request.args.get('seed'):
        seed = int(request.args.get('seed'))
    post = gen_obj.gen_post(seed)
    return jsonify(post),200
    

@api.route('/object/comment')
def gen_comment():
    seed = time.time()
    if request.args.get('seed'):
        seed = int(request.args.get('seed'))
    comment = gen_obj.gen_comment(seed)
    return jsonify(comment),200


@api.route('/bulk/posts/<int:num>')
def gen_posts(num=1):
    posts = gen_bulk.gen_posts(num)
    return jsonify(posts),200


@api.route('/bulk/comments/<int:num>')
def gen_comments(num=1):
    comments = gen_bulk.gen_comments(num)
    return jsonify(comments),200

@api.route('/bulk/profiles/<int:num>')
def gen_profiles(num=1):
    profiles = gen_bulk.gen_profiles(num)
    return jsonify(profiles),200

@api.route('/bulk/images/<int:num>')
def gen_images_list(num=1):
    images = gen_bulk.gen_images_list(num)
    return jsonify(images),200