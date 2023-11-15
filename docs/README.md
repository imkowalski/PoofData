| [Profile Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Object.md)  | [Selfhost](./Selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) | [About](./About.md) |

![img](./img/PoofData.png)

> A simple API, made for frontend developers to test and help develop ther UI/UX designs, by providing them dummy/placeholder data
<br>

# Quick start

You can either selfhost the project, or use the link for the API is:
````
https://poofdata-1-e0595391.deta.app
````  
This link is free to use, but there is a rate limit of 1 call per second, if you want to bypass this you should selfhost the project, to learn how to you can read more about it [her](./selfhost.md).

To get going you test if the api works by pinging /api/
````
https://poofdata-1-e0595391.deta.app/api/
```` 
and you should get a response that looks like this
````json
{
  "message": "I'm the Poof API",
  "status": 200
}
````

# Endpoints
Here is a list of all endpoints with a link to see the possible arguments for the diffrent endpoints
- [/api/image/gen_identicon/](https://imkowalski.github.io/PoofData/Images#apiimagegen_identicon)
- [/api/image/gen_image](https://imkowalski.github.io/PoofData/Images#apiimagegen_image)
- [/api/user/profile](https://imkowalski.github.io/PoofData/Personal#apiuserprofile)
- [/api/object/comment](https://imkowalski.github.io/PoofData/Object#apiobjectcomment)
- [/api/object/post](https://imkowalski.github.io/PoofData/Object#apiobjectpost)
- [/api/bulk/posts/](https://imkowalski.github.io/PoofData/Bulk#apibulkposts)
- [/api/bulk/profiles/](https://imkowalski.github.io/PoofData/Bulk#apibulkprofiles)
- [/api/bulk/images/](https://imkowalski.github.io/PoofData/Bulk#apibulkimages)

# Known Errors
- there is an error with bulk where the ids make the api endpoints fail. the error code is: ````File "/var/task/gen_data/gen_bulk.py", line 7, in gen_posts
posts.append(gen_obj.gen_post(time.time()+i))
File "/var/task/gen_data/gen_obj.py", line 31, in gen_post
"id": int(str(seed)[-6:]),
ValueError: invalid literal for int() with base 10: '.39185'````
_____
Made by [Michal Kowalski](https://github.com/imkowalski)
Licensed under the [MIT license](https://opensource.org/license/mit/)

