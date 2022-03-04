#!/usr/bin/python3
"""entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel

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

    """-------CONSOLE 0.01-------------"""
    def do_create(self, args):
        """Method create new instance"""
        if not args:
            print("** class name missing **")
        elif args not:
            print("** class doesn´t exist **")
        else:
            new_class = BaseModel()
            new_class.save()
            print(new_class.id)
    
    def do_show(self, args):
        """ Method show the representation
            of the instance
        """



if __name__ == '__main__':
    HBNBCommand().cmdloop()
