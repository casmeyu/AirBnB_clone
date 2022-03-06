# AirBnB Clone for Holberton School
This is a brief description of what this console is about

# Models
- ### **BaseModel**
    This is the base model from where every other object inherits
    
    Attributes:
        - **id(uuid4)**
        - **created_at(datetime)**
        - **updated_at(datetime)**
- ### **User**
- ### **Place**
- ### **City**
- ### **State**
- ### **Amenity**
- ### **Review**

## Usage
Here we can find all the commands available on the console and how to use them
(list)
- ### **all \?\<class\>\?**
#### **\<class\> is an optional parameter**

Returns a list with all objects in the system if not class is specified
Otherwhise it returns only the instance of said class

```
create BaseModel
4b4f1249-ff39-443e-af90-9199f7609a34
```

Errors:
  - If no class is specified
```
  create
  \*\* class name missing \*\*
```
- ### **show <class> \"\<id\>\"**
Prints the string representation of an instance of a given class
ex:

Errors:


- ### **destroy <class> \"\<id\>\"**
Deletes an instance of a given class

ex:

Errors:


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
