#!/usr/bin/python3
"""File that contains the command interpreter"""
import cmd
import argparse
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Using EOF"""
        return True

    def do_quiet(self, line):
        """Quiet for exit the command interpreter"""
        return True

    def empyline(self):
        """Passing when empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
