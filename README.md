# AirBnB Clone for Holberton School
This is a brief description of what this console is about

# Models
- ### **BaseModel**
    This is the base model from where every other object inherits
    
    ##### Attributes
    - id(uuid4)
    - created_at(datetime)
    - updated_at(datetime)
    ##### Methods
    - save()
        Stores the object instance into the data base
    - to_dict()
        Returns the dictionary representation of the object
- ### **User**
- ### **Place**
- ### **City**
- ### **State**
- ### **Amenity**
- ### **Review**

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

- ### **all \?\<class\>\?**
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
##### Errors:


- ### **destroy <class> \"\<id\>\"**
Deletes an instance of a given class

ex:

##### Errors:


- ### **update \<class\> \"\<id\>\" \"\<attribue_name\>\" <value\>**


Mention that we can also use it by classname
- ### **User.all()**
- ### **User.show(\"\<id\>\")**
- ### **user.destroy(\"\<id\>\")**
- ### **User.update(\"\<id\>\", \"\<attribute\>\" \<value\>)**

Installation
Clone this repo and execute the **./console.py** file

Camila Abdala <camila@abdala.net>
Martin Casamayou <martin@casamayou.net>
