#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd
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
            print('** class doesn\'t exists**')
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
            for key in objects:
                aux_key = key.split('.')[0]
                if line[0] == aux_key:
                    list_repr.append(str(objects[key]))

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
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        key = f'{line[0]}.{line[1]}'
        if key not in storage.all().keys():
            print("** not instance found **")
            return

        if len(line) < 3:
            print('** attribute name missing **')
            return

        if len(line) < 4:
            print('** value missing **')
            return

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

        obj = storage.all()[key]
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
