#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBTNCommand(cmd.Cmd):
    prompt = '(hbtn) '

    # object manipulation
    def do_create(self, command):
        """Creates an instance of the desired class
        Usage: create <class_name>
        """
        if len(command) < 1:
            print('** class name missing **')
            return
        try:
            line = command.split()
            new_obj = eval(f'{line[0]}()')
            new_obj.save()
            print(new_obj.id)
        except Exception as ex:
            print('** class doesn\'t exists **')

    def do_show(self, command):
        """Prints string representation of an instance of a class based on id
        Usage: show <class_name> <id>
        """
        if len(command) < 1:
            print('** class name missing **')
            return

        line = command.split()
        try:
            type(eval(line[0]))
        except Exception as ex:
            print('** class doesn\'t exist **')
            return

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
        print(f'destroying {line}')

    def do_all(self, command):
        """Prints the string representation of all the instances of a class
if no class is given it prints all the instances
Usage: all ?<class_name>?
        """
        objects = storage.all()
        if len(command) < 1:
            for key in objects:
                print(objects[key])
        else:
            line = command.split()
            for key in objects:
                aux_key = key.split('.')[0]
                if line[0] == aux_key:
                    print(objects[key])

    def do_update(self, command):
        """Updates instance of a class based on id adding/updating attributes
only one attribute can be updated at a time
Usage: update <class_name> <id> <attribute name> "<attribute value>"
        """
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
