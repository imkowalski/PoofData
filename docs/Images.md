| [Profile Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Object.md)  | [Selfhost](./Selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) |

![img](./img/PoofData.png)

# /api/image/gen_identicon/
````
/api/image/gen_identicon/<int:id>
````
This returns a identicon, it will always yield the same image given the same id, its the same priciple used by github to generate their Profile pictures.
An example output give the input of id 1 would be:

![image](./img/example%201.png)

Of course in some cases maybe you would need a specific size of an icon in that case you can use the URL-parameter size to get a specific image size up to 1024px
````
/api/image/gen_identicon/<int:id>?size=<int>
````
# /api/image/gen_image
````
/api/image/gen_image?width=<int>&height=<int>
````
This returns a simple one color image, it will always yield the same image with no variation, for example if these paramters are passed:
````
/api/image/gen_image?width=800&height=400
````
the resulting image would look like this:
![image](./img/gen_image_example_1.png)

_____
Made by [Michal Kowalski](https://github.com/imkowalski)
Licensed under the [GNU AGPLv3](https://github.com/imkowalski/PoofData/blob/main/LICENSE)