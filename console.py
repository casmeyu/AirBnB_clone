#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBTNCommand(cmd.Cmd):
    prompt = '(hbtn) '

    # validation functions
    def check_class(self, cls):
        print(cls)
        try:
            type(eval(cls))
            return True
        except Exception as ex:
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
        
        if self.check_class(line[0]):
            if len(line) < 2:
                print('** instance id missing **')
            elif len(line) < 3:
                print('** attribute name missing **')
            elif len(line) < 4:
                print('** value missing **')
            else:
                try:
                    key = f'{line[0]}.{line[1]}'
                    obj = storage.all()
                    obj = obj[key]
                    
                    if line[2] == 'created_at' and line[2] == 'updated_at':
                        return
                    if line[2] == 'id':
                        return
                    att = line[3].strip('\"')
                    print(f"stripped: {att}")
                    setattr(obj, 'updated_at', datetime.now())
                    setattr(obj, line[2], line[3].strip('\"'))
                except Exception as ex:
                    print('** no instance found **')
                    print(ex)

        print(f"update {line}")

    def do_quit(self, command):
        """Quit command to exit the program
Usage: quit
        """
        return True

    def do_EOF(self, command):
        """End of File exits the program
Usage: EOF
        """
        return True

    def emptyline(self):
        """Prints a new line"""
        pass


if __name__ == '__main__':
    HBTNCommand().cmdloop()
