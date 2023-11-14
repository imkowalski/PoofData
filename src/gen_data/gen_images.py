from PIL import Image
import random
from io import BytesIO

def gen_identicon(id,resolution=10, size=256):
    if size > 1024:
        return None
    
    img = Image.new('RGB', (resolution, resolution),color=(255,255,255))
    pixels = img.load()
    random.seed(id)
    color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
    
    for i in range(int(img.size[0]/2)):
        for j in range(int(img.size[1])):
            if random.randint(0, 1):
                pixels[i,j] = color
    right = img.crop((0, 0, int(resolution/2), resolution))
    right = right.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(right, (int(resolution/2), 0, resolution, resolution))
    img = img.resize((size,size),resample=Image.BOX)
    
    temp_img = BytesIO()
    img.save(temp_img, 'jpeg', quality=50)
    temp_img.seek(0)
    
    return temp_img