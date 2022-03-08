#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBTNCommand(cmd.Cmd):
    """Command line class"""
    prompt = '(hbnb) '

    def methods(self):
        """Dictionary of methods for command line"""
        methods = {}
        methods['all'] = self.do_all
        methods['show'] = self.do_show
        methods['destroy'] = self.do_destroy
        methods['update'] = self.do_update
        methods['count'] = self.count
        return(methods)

    def classes(self):
        """Dictionary of valid classes"""
        classes = {}
        classes['BaseModel'] = BaseModel
        classes['User'] = User
        classes['City'] = City
        classes['Amenity'] = Amenity
        classes['Place'] = Place
        classes['State'] = State
        classes['Review'] = Review
        return(classes)

    # validation functions
    def check_class(self, cls):
        """Check for the diffrent classes"""
        if cls in self.classes():
            return True
        else:
            print('** class doesn\'t exist **')
            return False

    # object manipulation
    def do_create(self, command):
        """Creates an instance of the desired class
Usage: create <class_name>
        """
        if len(command) < 1:
            print('** class name missing **')
            return
        line = command.split()

        if self.check_class(line[0]):
            new_obj = eval(f'{line[0]}()')
            new_obj.save()
            print(new_obj.id)

    def do_show(self, command):
        """Prints string representation of an instance of a class based on id
Usage: show <class_name> <id>
        """
        if len(command) < 1:
            print('** class name missing **')
            return

        line = command.split()
        if self.check_class(line[0]):
            if len(line) < 2:
                print('** instance id missing **')
                return
            try:
                line[1] = line[1].strip('\"')
                print(storage.all()[f'{line[0]}.{line[1]}'])
            except Exception as ex:
                print('** no instance found **')

    def do_destroy(self, command):
        """Deletes an instance of a class based on its id
and updates the data base
Usage: destroy <class_name> <id>
        """
        if len(command) < 1:
            print('** class name missing **')
            return

        line = command.split()

        if self.check_class(line[0]):
            if len(line) < 2:
                print('** instance id missing **')
                return

            try:
                del(storage.all()[f'{line[0]}.{line[1]}'])
                storage.save()
            except Exception as ex:
                print('** no instance found **')

    def do_all(self, command):
        """Prints the string representation of all the instances of a class
if no class is given it prints all the instances
Usage: all ?<class_name>?
        """
        objects = storage.all()
        list_repr = []
        if len(command) < 1:
            for key in objects:
                list_repr.append(str(objects[key]))
        else:
            line = command.split()
            if line[0] in self.classes().keys():
                for key in objects:
                    aux_key = key.split('.')[0]
                    if line[0] == aux_key:
                        list_repr.append(str(objects[key]))
            else:
                print("** class doesn't exist **")
                return

        print(list_repr)

    def do_update(self, command):
        """Updates instance of a class based on id adding/updating attributes
only one attribute can be updated at a time
Usage: update <class_name> <id> <attribute name> "<attribute value>"
        """
        if len(command) < 1:
            print('** class name missing **')
            return

        line = command.split()

        if not self.check_class(line[0]):
            return None

        if len(line) < 2:
            print("** instance id missing **")
            return None
        line[1] = line[1].strip(",")
        line[1] = line[1].strip('\"')
        key = f'{line[0]}.{line[1]}'
        if key not in storage.all().keys():
            print("** no instance found **")
            return None

        if len(line) < 3:
            print('** attribute name missing **')
            return None

        if len(line) < 4:
            print('** value missing **')
            return None
        
        obj = storage.all()[key]

        if line[2][0] == "{":
            str_dict = ""
            for i in range(2, len(line)):
                for char in line[i]:
                    if char == "\'":
                        str_dict += '\"'
                    else:
                        str_dict += char

            # print(f'str_dict {str_dict}')
            try:
                attr_dict = json.loads(str_dict)
                for key, value in attr_dict.items():
                    setattr(obj, key, value)
            except Exception as ex:
                raise(ex)
        else:
            line[2] = line[2].strip(',')
            line[2] = line[2].strip('\"') 
            if line[2] == 'created_at' and line[2] == 'updated_at':
                return
            if line[2] == 'id':
                return

            value = line[3]
            if value[0] != '\"' and (value[0].isdigit() or value[0] == '.'):
                float_flag = False
                for char in value:
                    if char.isdigit() or char == '.':
                        if char == '.':
                            float_flag = True
                    else:
                        break

                if float_flag:
                    value = float(value)
                else:
                    value = int(value)
            else:
                value = value.strip('\"')

            setattr(obj, 'updated_at', datetime.now())
            setattr(obj, line[2], value)

        storage.save()

    # Specific object Manipulation
    def default(self, command):
        """Check any input for valid command"""
        if len(command) < 1:
            return
        line = command.split('.')
        
        if self.check_class(line[0]):
            if len(line) > 1:

                fun = line[1].split('(')
                if fun[0] in self.methods().keys():
                    if len(fun) > 1:
                        fun[1] = fun[1].strip(')')
                        self.methods()[fun[0]](f"{line[0]} {fun[1]}")
                    else:
                        return

    def count(self, command):
        """Count command to retrieve the number of instances"""

        line = command.split(' ')

        count = 0

        for key in storage.all():
            key = key.split('.')
            if key[0] == line[0]:
                count += 1
        print(count)

    def do_quit(self, command):
        """Quit command to exit the program
Usage: quit
        """
        return True

    def do_EOF(self, command):
        """End of File exits the program
Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """Prints a new line"""
        return


if __name__ == '__main__':
    HBTNCommand().cmdloop()
