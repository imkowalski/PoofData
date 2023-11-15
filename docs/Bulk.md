| [Profile Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Object.md)  | [Selfhost](./Selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) | [About](./About.md) |

![img](./img/PoofData.png)

# /api/bulk/posts/
````
/api/bulk/posts/<int:num>
````
this will return a JSON object with a list of posts
if we take for example 2 posts, the request URL would look like this:
````
/api/bulk/posts/2
````
And the result would look like this:
````json
[
  {
    "author_id": 931,
    "comments_ids": [
      9076,
      9268,
      2728,
      9836,
      1180,
      6114,
      2924,
      1111,
      4990,
      7827,
      8778,
      4082,
      1519,
      3990,
      8174,
      8054
    ],
    "date": 1700081227.1131585,
    "dislikes": 633,
    "id": 130977,
    "likes": 674,
    "text": "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat ea necessitatibus labore vel consequuntur voluptatem. Nam amet vero quo perferendis magni aut voluptate consequatur ex voluptatem aperiam sed consequatur nobis. "
  },
  {
    "author_id": 386,
    "comments_ids": [
      8069,
      5845,
      2676,
      5293,
      6011,
      9357,
      2509,
      8793,
      4092,
      3816,
      9883,
      8092,
      9543,
      3940,
      6067,
      727,
      637,
      3892,
      2632
    ],
    "date": 1700081227.1132054,
    "dislikes": 485,
    "id": 131601,
    "likes": 348,
    "text": "Lorem ipsum dolor sit amet. Aut maiores laborum non suscipit quae qui tempore repellat ea necessitatibus labore vel consequuntur voluptatem. Nam amet vero quo perferendis magni aut voluptate consequatur ex voluptatem aperiam sed consequatur nobis. "
  }
]

````

# /api/bulk/profiles/
````
/api/bulk/profiles/<int:num>
````
this will return a JSON object with a list of profiles
if we take for example 2 profiles, the request URL would look like this:
````
/api/bulk/profiles/2
````
And the result would look like this:
````json
[
  {
    "company": "Reading Inc",
    "email": "mason@poofdata.com",
    "id": 1700081483.5061908,
    "job": "Unemployed",
    "name": "Mason Kennedy",
    "phone": "02997396"
  },
  {
    "company": "Library Co",
    "email": "gabriel@poofdata.com",
    "id": 1700081484.5063045,
    "job": "Engineer",
    "name": "Gabriel Cox",
    "phone": "01478871"
  }
]
````

# /api/bulk/images/
````
/api/bulk/images/<int:num>
````
this will return a JSON object with a list of images
if we take for example 2 images, the request URL would look like this:
````
/api/bulk/images/2
````
And the result would look like this:
````json
[
  {
    "id": 281188,
    "image": "/image/gen_image?width=512&height=512"
  },
  {
    "id": 281275,
    "image": "/image/gen_image?width=512&height=512"
  }
]
````
_____
Made by [Michal Kowalski](https://github.com/imkowalski)
Licensed under the [MIT license](https://opensource.org/license/mit/)