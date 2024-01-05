| [Profile Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Object.md)  | [Selfhost](./Selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) |

![img](./img/PoofData.png)

# /api/object/post
````
/api/object/post
````
this will return a JSON object that is an example of a typical post. The object would look something like this:
````json
{
  "author_id": 725,
  "comments_ids": [
    6185,
    6494,
    104,
    1969,
    7303
  ],
  "date": 1700078741.7399404,
  "dislikes": 134,
  "id": 397783,
  "likes": 967,
  "text": "Lorem ..."
}
````
> \**note: The text field is quite a bit longer*

This will by deafult return a randomly generated, post.
If you want  a post with a specific id you can use the URL-paramter seed
````
/api/object/post?seed=<int>
````
For example if the seed int was a 1, the output would always be
````json
{
  "author_id": 780,
  "comments_ids": [
    9326,
    1034,
    4180,
    1932,
    8118
  ],
  "date": 1700079094.49546,
  "dislikes": 484,
  "id": 1,
  "likes": 461,
  "text": "Lorem ..."
}
````


# /api/object/comment
````
/api/object/comment
````
this will return a JSON object that is an example of a typical comment. The object would look something like this:
````json
{
  "author_id": 361,
  "comments_ids": [
    33,
    53,
    67,
    76
  ],
  "date": 1700079279.6495888,
  "dislikes": 133,
  "id": 494715,
  "likes": 640,
  "text": "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat."
}
````

This will by deafult return a randomly generated, comment.
If you want a comment with a specific id you can use the URL-paramter seed
````
/api/object/comment?seed=<int>
````
For example if the seed int was a 1, the output would always be
````json
{
  "author_id": 868,
  "comments_ids": [
    73
  ],
  "date": 1700079441.9421806,
  "dislikes": 783,
  "id": 1,
  "likes": 822,
  "text": "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat."
}
````
_____
Made by [Michal Kowalski](https://github.com/imkowalski)
Licensed under the [GNU AGPLv3](https://github.com/imkowalski/PoofData/blob/main/LICENSE)