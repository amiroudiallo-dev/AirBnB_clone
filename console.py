#!/usr/bin/python3
"""
This the command line interpre ter module using cmd."""

import cmd


class HBNBCommand(cmd.Cmd):
    """ hbnh command line interpreter class """

    def __init__(self):
        super().__init__()
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ EOF command disconnects the program """
        print("disconnected...")
        return True

    def emptyline(self):
        """ called when an empty line is entered """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

