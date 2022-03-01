#!/usr/bin/python3
""" Command Interpreter Module
    This module is the entry point for the logic of the application
    It uses the CMD python module
"""
import cmd


class HBTNCommand(cmd.Cmd):
    prompt = '(hbtn) '

    def do_quit(self, command):
        """quit - exits the program"""
        print('quitting')
        return True

    def do_EOF(self, command):
        """end of file - exits the program"""
        return True



if __name__ == '__main__':
    HBTNCommand().cmdloop()
