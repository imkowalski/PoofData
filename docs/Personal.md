| [Personal Information Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Objekt.md)  | [How To Selfhost?](./selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) |

<br><br><br>

![img](./img/PoofData.png)

# /api/user/profile
````
/api/user/profile
````
by deafult this will return a a JSON object with a random person profile information, this would look like this
````json
{
  "company": "Bat Industries",
  "email": "korbin860@poofdata.com",
  "id": 632235,
  "job": "Artist",
  "name": "Korbin Knapp",
  "phone": "62302978"
}
````
If you want to get the same person you can use URL-parameters to set specific seed like this:
````
/api/user/profile?seed=1
````
This will allways yield the same output, in that case the seedwill be used as the id, that will look like this:
````json
{
  "company": "Bath Media",
  "email": "hendrix@poofdata.com",
  "id": 1,
  "job": "Designer",
  "name": "Hendrix Kirk",
  "phone": "29141777"
}
````
If you only want some specific fields from this endpoints you can use URL-parameters to specify which parameters you want to get. The availible parameters are:
- company
- email
- id 
- job
- name
- phone

these can of course be chained. If you for an example weanted to only get the name and email of person with the id 6 you could write
````
/api/user/profile?email&name&seed=6
````
this would yield this result:
````json
{
  "email": "capri@poofdata.com",
  "name": "Capri Boone"
}
````
The order of the parameters doesn't matter