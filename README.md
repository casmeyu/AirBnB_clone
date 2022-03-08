# AirBnB Clone for Holberton School
This program storage the data of the differents classes (User, Place, Amenity, City, State, Review) that inherit form BaseModel, and is managed for the class FlieStorage.

# Models
- ### **BaseModel**
    This is the base model from where every other object inherits
    
  ##### Attributes:
    - **id(uuid4)**
    - **created_at(datetime)**
    - **updated_at(datetime)**
 ##### Methods
    - save()
        Stores the object instance into the data base
    - to_dict()
        Returns the dictionary representation of the object
- ### **User**
   Is the information of the client 
  
   Attributes:
    - **email(string)**
    - **password(string)**
    - **first_name(string)**
    - **last_name(string)**

- ### **Place**
  The place of the lodging
  Attributes:
   - **city_id(uuid4)**
   - **user_id(uuid4)**
   - **name(string)**
   - **description(string)**
   - **number_rooms(int)**
   - **number_bathrooms(int)**
   - **max_guest(int)**
   - **price_by_night(int)**
   - **latitude(float)**
   - **longitude(float)**
   - **amenity_ids(list)**

- ### **City**
  The City of the lodging
  
  Attributes:
   - **city_id(uuid4)**
   - **name(string)**

- ### **State**
  The State of the lodging

  Attributes:
   - **name(string)**

- ### **Amenity**
  The amenity of the lodging
  
  Attribute:
   - **name(string)**

- ### **Review**
  Review of the lodging

  Attribute:
   - **place_id(uuid4)**
   - **user_id(uuid4)**
   - **text(string)**

## Usage
Here we can find all the commands available on the console and how to use them
- ### **create <class>**
    Creates an instance of a class with the basic attributes, saves it into the data base
    and prints it's id

##### Examples:
```
create BaseModel
4b4f1249-ff39-443e-af90-9199f7609a34
create User
0d7fe5d8-2134-40e3-ada5-f6865b532a8d
```

##### Errors:
- **No class is specified**
```
  create
  ** class name missing **
```

- ### **all \<class\>**
    ##### \<class\> is an optional parameter

    Returns a list with all objects in the system if no class is specified
    Otherwhise, if the class exists, returns a list only with the instances of said class
##### Examples:
```
all
["[BaseModel] (4b4f1249-ff39-443e-af90-9199f7609a34) {'id': '4b4f1249-ff39-443e-af90-9199f7609a34', 'created_at': datetime.datetime(2022, 3, 6, 13, 16, 39, 570451), 'updated_at': datetime.datetime(2022, 3, 6, 13, 16, 39, 570466)}", "[User] (0d7fe5d8-2134-40e3-ada5-f6865b532a8d) {'id': '0d7fe5d8-2134-40e3-ada5-f6865b532a8d', 'created_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577397), 'updated_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577410)}"]
```
```
all User
["[User] (0d7fe5d8-2134-40e3-ada5-f6865b532a8d) {'id': '0d7fe5d8-2134-40e3-ada5-f6865b532a8d', 'created_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577397), 'updated_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577410)}"]
```

##### Errors:
**No class found**
```
all NotAClass
** class doen's exist **
```

- ### **show <class> \"\<id\>\"**
Prints the string representation of an instance of a given class
It checks if it's a valid class and then if the instance exists

##### Examples:
```
show User 0d7fe5d8-2134-40e3-ada5-f6865b532a8d
["[User] (0d7fe5d8-2134-40e3-ada5-f6865b532a8d) {'id': '0d7fe5d8-2134-40e3-ada5-f6865b532a8d', 'created_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577397), 'updated_at': datetime.datetime(2022, 3, 6, 13, 39, 39, 577410)}"]
```
```
 show Place fec9663f-ff87-4c72-8c1b-54025762cd9a
[Place] (fec9663f-ff87-4c72-8c1b-54025762cd9a) {'id': 'fec9663f-ff87-4c72-8c1b-54025762cd9a', 'created_at': datetime.datetime(2022, 3, 6, 14, 8, 12, 760424), 'updated_at': datetime.datetime(2022, 3, 6, 14, 8, 12, 760443)}
```
##### Errors:
```
 show
** class name missing **
```
```
show Pla
** class doesn't exist **
```
```
 show User
** instance id missing **
```
```
 show User 673habs9j
** no instance found **
```

- ### **destroy <class> \"\<id\>\"**
Deletes an instance of a given class

##### Examples:
```
destroy User 4c2ff496-c3c5-4745-926c-75a7ab4b5ec1
```

##### Errors:
```
destroy Use
** class doesn't exist **
```
```
 destroy User
** instance id missing **
```
```
 destroy User 673habs9j
** no instance found **
```

- ### **update \<class\> \"\<id\>\" \"\<attribue_name\>\" <value\>**
  ##### \<class\> is an optional parameter
  
  Updates an instance based on the class name and id by adding or updating atribute

##### Examples:
```
update User 050b35d1-837c-408b-a9af-5bda209b5367 email "user@user.com"
show User 050b35d1-837c-408b-a9af-5bda209b5367
[User] (050b35d1-837c-408b-a9af-5bda209b5367) {'email': 'user@user.com', 'password': '', 'first_name': '', 'last_name': '', 'id': '050b35d1-837c-408b-a9af-5bda209b5367', 'created_at': datetime.datetime(2022, 3, 3, 11, 45, 33, 709606), 'updated_at': datetime.datetime(2022, 3, 6, 14, 20, 23, 860633), 'name': 'nacho'}
```

##### Errors:
```
 update User 050b35d1-837c-408b-a9af-5bda209b5367 email
** value missing **
```
```
update User 050b35d1-837c-408b-a9af-5bda209b5367
** attribute name missing **
```
```
update User 050b35d1-837c-408b-a9af-5bd
** not instance found **
```

- ### **User.all()**
 Returns a list with all objects in the system if no class is specified
    Otherwhise, if the class exists, returns a list only with the instances of said class

##### Examples:
```
User.all()
["[User] (050b35d1-837c-408b-a9af-5bda209b5367) {'email': 'user@user.com', 'password': '', 'first_name': '', 'last_name': '', 'id': '050b35d1-837c-408b-a9af-5bda209b5367', 'created_at': datetime.datetime(2022, 3, 3, 11, 45, 33, 709606), 'updated_at': datetime.datetime(2022, 3, 6, 14, 20, 23, 860633), 'name': 'nacho'}", "[User] (eadb8f8c-a24a-47f2-968b-1a71240711c3) {'id': 'eadb8f8c-a24a-47f2-968b-1a71240711c3', 'created_at': datetime.datetime(2022, 3, 4, 23, 2, 7, 60520), 'updated_at': datetime.datetime(2022, 3, 4, 23, 2, 7, 60533), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}", "[User] (6682f221-62cc-46b2-b651-db1f971903a6) {'id': '6682f221-62cc-46b2-b651-db1f971903a6', 'created_at': datetime.datetime(2022, 3, 5, 6, 16, 11, 960301), 'updated_at': datetime.datetime(2022, 3, 5, 6, 16, 11, 960319)}"]
```
```
 Place.all()
["[Place] (da7a1223-00f4-4180-bdc8-87ff0fbab200) {'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0, 'latitude': 0.0, 'longitude': 0.0, 'amenity_ids': [], 'id': 'da7a1223-00f4-4180-bdc8-87ff0fbab200', 'created_at': datetime.datetime(2022, 3, 3, 11, 52, 32, 507321), 'updated_at': datetime.datetime(2022, 3, 3, 11, 52, 32, 507333)}", "[Place] (fec9663f-ff87-4c72-8c1b-54025762cd9a) {'id': 'fec9663f-ff87-4c72-8c1b-54025762cd9a', 'created_at': datetime.datetime(2022, 3, 6, 14, 8, 12, 760424), 'updated_at': datetime.datetime(2022, 3, 6, 14, 8, 12, 760443)}"]
```

##### Errors:
```
 Pl.all()
** class doesn't exist **
```

- ### **User.show(\"\<id\>\")**
Prints the string representation of an instance of a given class
It checks if it's a valid class and then if the instance exists

##### Example:
```
BaseModel.show(a8d2d3d2-fb60-4470-acb7-d47dddc168ab)
[BaseModel] (a8d2d3d2-fb60-4470-acb7-d47dddc168ab) {'id': 'a8d2d3d2-fb60-4470-acb7-d47dddc168ab', 'created_at': datetime.datetime(2022, 3, 3, 11, 44, 39, 609820), 'updated_at': datetime.datetime(2022, 3, 3, 11, 44, 39, 610073), 'name': 'My First Model', 'my_number': 89}
```

##### Errors:
```
BaseModel.show()
** instance id missing **
```
```
Basemodel.show()
** class doesn't exist **
```
- ### **Class.destroy(\"\<id\>\")**
Deletes an instance of a given class

##### Example:
```
BaseModel.destroy(a8d2d3d2-fb60-4470-acb7-d47dddc168ab)
BaseModel.all()
["[BaseModel] (8056187e-84d6-4546-87a0-ceff452dc39f) {'id': '8056187e-84d6-4546-87a0-ceff452dc39f', 'created_at': datetime.datetime(2022, 3, 3, 11, 45, 2, 608731), 'updated_at': datetime.datetime(2022, 3, 3, 11, 45, 2, 608743), 'name': 'My_First_Model', 'my_number': 89}"]
```

##### Error:
```
 BaseModel.destroy()
** instance id missing **
```
```
 BaseModel.destroy(673habs9j)
** no instance found **
```

- ### **User.update(\"\<id\>\", \"\<attribute\>\" \<value\>)**


##### Example:
```
User.update(eadb8f8c-a24a-47f2-968b-1a71240711c3, "name", "Martin")
User.show(eadb8f8c-a24a-47f2-968b-1a71240711c3)
[User] (eadb8f8c-a24a-47f2-968b-1a71240711c3) {'id': 'eadb8f8c-a24a-47f2-968b-1a71240711c3', 'created_at': datetime.datetime(2022, 3, 4, 23, 2, 7, 60520), 'updated_at': datetime.datetime(2022, 3, 6, 14, 37, 25, 860372), 'email': '', 'password': '', 'first_name': '', 'last_name': '', 'name': 'Martin'}
```

##### Errors:
```
 User.update(eadb8f8c-a24a-47f2-968b-1a71240711c3, name)
** value missing **
```
```
User.update(eadb8f8c-a24a-47f2-968b-1a7124071)
** not instance found **
```

## Installation
Clone this repo and execute the **./console.py** file
```
 git clone https://github.com/ojo-perezoso/AirBnB_clone
 cd AirBnB_clone
 ./console.py
```

Camila Abdala <3962@holbertonschool.com>
Martin Casamayou <martin@casamayou.net>
