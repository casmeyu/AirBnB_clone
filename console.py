#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd


class HBTNCommand(cmd.Cmd):
    prompt = '(hbtn) '

    def do_quit(self, command):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, command):
        """End of File exits the program"""
        return True

    def emptyline(self):
        """Prints a new line"""
        pass


if __name__ == '__main__':
    HBTNCommand().cmdloop()
