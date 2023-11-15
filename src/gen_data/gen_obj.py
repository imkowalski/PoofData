import random,time


def gen_comment(seed):
    random.seed(seed)
    text = "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat."
    ids = []
    for i in range(0,random.randint(0,4)):
        ids.append(random.randint(1,100))
    
    return {
        "text": text,
        "id": int(str(seed)[-6:]),
        "author_id": random.randint(1,1000),
        "likes": random.randint(1,1000),
        "dislikes": random.randint(1,1000),
        "date": time.time(),
        "comments_ids": ids
    }
    

def gen_post(seed):
    random.seed(seed)
    text = "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat ea necessitatibus labore vel consequuntur voluptatem. Nam amet vero quo perferendis magni aut voluptate consequatur ex voluptatem aperiam sed consequatur nobis. "
    ids = []
    for i in range(0,random.randint(1,20)):
        ids.append(random.randint(1,10000))
    
    return {
        "text": text,
        "id": int(str(seed)[-6:]),
        "author_id": random.randint(1,1000),
        "likes": random.randint(1,1000),
        "dislikes": random.randint(1,1000),
        "date": time.time(),
        "comments_ids": ids
    }
    