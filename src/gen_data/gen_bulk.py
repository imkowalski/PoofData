from gen_data import gen_images, gen_text, gen_obj, gen_bulk
import time

def gen_posts(num):
    posts = []
    for i in range(0,num):
        posts.append(gen_obj.gen_post(time.time()+i))
    return posts

def gen_comments(num):
    comments = []
    for i in range(0,num):
        comments.append(gen_obj.gen_comment(time.time()+i))
    return comments

def gen_profiles(num):
    profiles = []
    for i in range(0,num):
        profiles.append(gen_text.gen_profile(time.time()+i))
    return profiles

def gen_images_list(num):
    images = []
    for i in range(0,num):
        images.append({"image":"/image/gen_image?width=512&height=512","id": int(str(time.time())[-7:])+i})
    return images