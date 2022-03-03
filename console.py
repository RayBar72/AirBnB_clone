#!/usr/bin/python3
"""File that contains the command interpreter"""
import cmd
import argparse
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """Creates an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            x = BaseModel()
            x.save()
            print(x.id)

    def do_show(self, line):
        """
        String representation of an instance
        based on the name and id. It is printed
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            tokens = line.split(" ")
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(tokens[0], tokens[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file).
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            tokens = line.split(" ")
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(tokens[0], tokens[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if line != "":
            tokens = line.split(" ")
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
        for k in storage.all():
            print(storage.all()[k])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file).
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            tokens = line.split(" ")
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            elif len(tokens) < 3:
                print("** attribute name missing **")
            elif len(tokens) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(tokens[0], tokens[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    setattr(storage.all()[key], tokens[2], tokens[3])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
