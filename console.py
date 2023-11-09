#!/usr/bin/env python3
# This Class define the entry point of a command interpreter
"""Represent class cmd"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb) '

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
    
    #def precmd(self, line):
     #   """Define instructions to be executed before <line>
      #  interpretation
       # """
        #if not line:
         #   return '\n'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
