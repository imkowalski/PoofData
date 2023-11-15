| [Personal Information Endpoints](./Personal.md)  | [Image Endpoints](./Images.md)  | [Bulk Data Endpoints](./Bulk.md) | [Object Endpoints](./Objekt.md)  | [How To Selfhost?](./selfhost.md) | [Github Repo](https://github.com/imkowalski/PoofData) |<br><br><br>

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
If you want to get the same person you can use URL parameters to set s specific seed like this:
````
/api/user/profile?seed=1
````
This will allways yield the same output, that will look like this:
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