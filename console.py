#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd


class HBTNCommand(cmd.Cmd):
    prompt = '(hbtn) '

    # object manipulation
    def do_create(self, line):
        """Creates an instance of the desired class
        Usage: create <class_name>
        """
        print(f"creating {line}")

    def do_show(self, line):
        """Prints string representation of an instance of a class based on id
Usage: show <class_name> <id>
        """
        print(f"show {line}")

    def do_destroy(self, line):
        """Deletes an instance of a class based on its id
and updates the data base
Usage: destroy <class_name> <id>
        """
        print(f'destroying {line}')

    def do_all(self, line):
        """Prints the string representation of all the instances of a class
if no class is given it prints all the instances
Usage: all ?<class_name>?
        """
        if not line:
            print("show all")
        else:
            print(f"all {line}")

    def do_update(self, line):
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
