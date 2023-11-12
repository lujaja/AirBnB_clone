#!/usr/bin/env python3
# This Class define the entry point of a command interpreter
"""Represent class cmd"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb) '

    def check_errors(self, line, num_arg):
        """parsesthe line to check if their exist any bug inregard to
        the expected input

        Attributes:
            line (arguments): lineinput
        """
        msg = [
                "** class name missing **",
                "** class doesn't exist **",
                "** instance id missing **",
                "** no instance found **",
                "** attribute name missing **",
                "** value missing **"
        ]

        class_names = {
                "BaseModel": "BaseModel",
                "User": "User",
                "State": "State",
                "City": "City",
                "Amenity": "Amenity",
                "Place": "Place",
                "Review": "Review"
            }

        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_arg >= 1 and args[0] not in class_names.keys():
            print(msg[1])
            return 1
        elif num_arg == 1:
            return 0
        if num_arg >= 2 and len(args) < 2:
            return 1
        dict = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + "." + args[1]
        if num_arg >= 2 and key not in dict:
            print(msg[3])
            return 1
        elif num_arg == 2:
            return 0
        if num_arg >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_arg >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF exits the program"""
        return True

    def emptyline(self):
        """overrides the default empty line action"""
        pass

    def do_help(self, arg):
        """To get help on command type help <topic>
        """
        return super().do_help(arg)

    def do_create(self, line):
        """Create a new basemodel instance"""
        if (self.check_errors(line, 1) == 1):
            return
        args = line.split(" ")
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """show all instances under a given class"""
        if (self.check_errors(line, 2) == 1):
            return
        args = line.split()
        dic = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + "." + args[1]
        print(dic[key])

    def do_destroy(self, line):
        """delete an instance"""
        if (self.check_errors(line, 2) == 1):
            return
        args = line.split()
        dic = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + "." + args[1]
        del dic[key]
        storage.save()

    def do_all(self, line):
        """print all string representation of all instances based or not
        on the class name
        """
        dic = storage.all()
        args = line.split()
        if not line:
            print([str(x) for x in dic.values()])
            return
        if (self.check_errors(line, 1) == 1):
            return
        print([str(v) for v in dic.values() if v.__class__.__name__ ==
               args[0]])

    def do_update(self, line):
        """update an instance based on class name and id by adding or
        updating attribue
        """
        if (self.check_errors(line, 4) == 1):
            return
        args = line.split()
        dic = storage.all()
        for i in range(len(args[i:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + "." + args[i]
        attr_k = args[2]
        attr_v = args[3]
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except Exception:
            pass
        class_name = type(div[key]).__dict__
        if attr_k in class_name.keys():
            try:
                attr_v = type(class_name[attr_k])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(dic[key], attr_k, attr_v)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
