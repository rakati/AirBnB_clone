#!/usr/bin/python3
'''
Console Module
'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class'''

    prompt = '(hbnb) '

    def do_create(self, arg):
        '''This command creates a new instance of a specified class,
        saves it to the JSON file, and prints the ID of the new instance.'''

        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''This command prints the string representation of an instance
           based on the class name and ID provided.'''

        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''This command deletes an instance based on the class name and
           ID provided and saves the change into the JSON file.'''

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''This command prints the string representation of all instances
           based on the class name provided or all instances
           if no class name is provided.'''

        if not arg:
            print([str(value) for value in storage.all().values()])
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items(
                        ) if key.split('.')[0] == arg])

    def do_update(self, arg):
        '''This command updates an instance based on the class name, ID,
        attribute name, and attribute value provided,
        saving the change into the JSON file.'''

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_quit(self, arg):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''

        print()
        return True

    def emptyline(self):
        '''Called when an empty line is entered'''

        pass

    def default(self, line):
        '''special lines that need different treatment'''
        cmd = line.split('.')
        if len(cmd) != 2:
            print("*** Unkown syntax:", line)
        elif cmd[0] not in storage.classes():
            print(f"** {cmd[0]} class doesn't exist **")
        elif cmd[1] == "all()":
            print([str(value) for key, value in storage.all().items(
                        ) if key.split('.')[0] == cmd[0]])
        else:
            print("** class method not supported **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
