#!/usr/bin/python3
"""File that contains the command interpreter"""
import cmd
from itertools import count
import string
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Using EOF"""
        print()
        return True

    def do_quit(self, line):
        """Quit for exit the command interpreter"""
        return True

    def emptyline(self):
        """Passing when empty line"""
        pass

    def do_create(self, line):
        """Creates an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split()
            try:
                x = eval(args[0])()
                x.save()
                print(x.id)
            except Exception as e:
                print("** class doesn't exist **")

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
                    t3 = tokens[3].strip('\"')
                    if hasattr(key, tokens[2]) is True:
                        att_t = type(getattr(key, tokens[2]))
                        if att_t == int:
                            setattr(storage.all(key), tokens[2], int(t3))
                            storage.save()
                        elif att_t == float:
                            setattr(storage.all(key), tokens[2], float(t3))
                            storage.save()
                    else:
                        setattr(storage.all()[key], tokens[2], tokens[3])
                        storage.save()

    def do_count(self, line):
        """Retrives the number of instances in a class"""
        compara = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
        if line in compara:
            i = 0
            j_obj = storage.all()
            for k, v in j_obj.items():
                if line in k:
                    i += 1
            print(i)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Method called when an input line commmand is not recognaized"""
        compara = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
        for c in compara:
            tokens = line.split(".")
            tokens_par1 = tokens[1].split("(")
            tokens_par2 = tokens_par1[1].split(")")
            tokens_com = tokens_par2[0].split('"')
            c_all = c + ".all()"
            c_count = c + ".count()"
            c_show = c + ".show(" + tokens_par2[0] + ")"
            c_destroy = c + ".destroy(" + tokens_par2[0] + ")"
            if line == c_all:
                line = "all " + tokens[0]
                HBNBCommand.do_all(self, line)
                break
            elif line == c_count:
                line = tokens[0]
                HBNBCommand.do_count(self, line)
                break
            elif line == c_show:
                line = tokens[0] + " " + tokens_com[1]
                HBNBCommand.do_show(self, line)
                break
            elif line == c_destroy:
                line = tokens[0] + " " + tokens_com[1]
                HBNBCommand.do_destroy(self, line)
                break


if __name__ == "__main__":
    HBNBCommand().cmdloop()
