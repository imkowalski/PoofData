| [Profile Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Objekt.md)  | [Selfhost](./Selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) | [About](./About.md) |

![img](./img/PoofData.png)

# How to host your own version

This is a guide how to download and run this project
## Download

Firstly either directly download the github repo from the github or use git or gh cli to download the repo.

Using git:
````bash
git clone https://github.com/imkowalski/PoofData.git
````

Using the github CLI:
````bash
gh repo clone imkowalski/PoofData
````

## Run
Firstly navigate into the newly created folder
````bach
cd ./PoofData
````
Then you have two options to run this project.

### Using Deta Space
The first method depends on [deta.space](https://deta.space/) if you have an account and the [space cli](https://deta.space/docs/en/build/fundamentals/space-cli/) you can either push it using the push command:
````bash
space push
````
Which should proptly begin to upload this to your deta space cloud.
Or run it locally using you can use the dev command:
````bash
space dev
````
Which should run locally and open a flask instace at port 8000 (can be changed in the dev.py file)
### Guvicorn and Python interpreter
Another way you can run this is using a guvicorn compatible system (aka. not windows), you can use the guvicorn package and in the src folder run:
````bash
guvicorn main:app
````
To run this locally you can just navigate to the src folder and just run the dev.py file
````bash
python3 dev.py
````

_____
Made by [Michal Kowalski](https://github.com/imkowalski)
Licensed under the [GNU AGPLv3](https://github.com/imkowalski/PoofData/blob/main/LICENSE)
