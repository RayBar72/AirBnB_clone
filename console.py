#!/usr/bin/python3
"""entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Creation of class"""
    prompt = '(hbnb)'

    def emptyline(self):
        """EmptyLine"""
        pass
    
    def do_quit(self, line):
        """Quit command to EXIT the program"""
        return True

    def do_EOF(self, line):
        """Exit using ctrl + C"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
