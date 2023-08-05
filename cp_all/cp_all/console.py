#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review



class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __classes = ["BaseModel",
            "User",
            "Place",
            "City",
            "Amenity",
            "Review"]

    def do_quit(self, line):
        '''Quit command to exit the progrm
        '''
        return True

    def do_EOF(self, line):
        '''EOF signal to exit program
        '''
        return True

    def emptyline(self):
        return

    def do_create(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)
        storage.save()
    
    def do_show(self, arg):
        args = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        
        elif len(args) == 1:
            print("** instance id missing **")

        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])
    
    def do_destroy(self, arg):
        args = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif args[0] not in self.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()

    def do_all(self, arg):
        args = arg.split()

        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])

        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        
        else:
            print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])

    def do_update(self, arg):
        args = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif args[0] not in self.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif f"{args[0]}.{args[1]}" not in storage.all():
#        elif args[0].args[1] not in storage.all():
            print("** no instance found **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")
        
        else:
            obj_class = args[0]
            obj_id = args[1]
            obj_key = obj_class + "." + obj_id
            obj = storage.all()[obj_key]

            attr_name = args[2]
            attr_value = args[3]

            if attr_value[0] == '"':
                attr_value = attr_value[1:-1]

            if hasattr(obj, attr_name):
                type_ = type(getattr(obj, attr_name))
                
                if type_ in [str, float, int]:
                    attr_value = type_(attr_value)
                    setattr(obj, attr_name, attr_value)

            else:
                setattr(obj, attr_name, attr_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
