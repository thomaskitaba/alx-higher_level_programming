#!/usr/bin/python3
""" Base Class """
import json
import csv

class Base:
    """ description goes here """
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string representation
            of list_dictionaries
        """
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ json string to file """
        to_be_saved = []
        file_name = str(cls.__name__) + ".json"
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    temp = obj.to_dictionary()
                    to_be_saved.append(temp)
                f.write(Base.to_json_string(to_be_saved))

    @staticmethod
    def from_json_string(json_string):
        """ convert json string to python object """
        if json_string is None or json_string == "[]":
            return ([])

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create instance from ditionary """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ file to instance """
        file_name = str(cls.__name__) + ".json"
        file_instance = []
        try:
            with open(file_name, 'r') as f:
                p_obj = Base.from_json_string(f.read())

                for obj in p_obj:
                    new = cls.create(**obj)
                    file_instance.append(new)
                return file_instance
        except Exception as e:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save list objects [r1, r2] to csv file"""
        file_name = f"{cls.__name__}.csv"
        list_dict = []
        with open(file_name, 'w', newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
                fieldnames = ""
            else:
                fieldnames = list_objs[0].to_dictionary().keys()
            dict_writer = csv.DictWriter(csv_f, fieldnames=fieldnames)

            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            dict_writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """ load from csv file
        """
        file_name = f"{cls.__name__}.csv"
        created_list = []
        try:
            with open(file_name, 'r') as csv_f:

                if cls.__name__ == "Rectangle":
                    titles = ["id", "width", "height", "x", "y"]
                else:
                    titles = ["id", "size", "x", "y"]
                dict_reader = csv.DictReader(csv_f, fieldnames=titles)

                # convert dict_reader to correct format
                new_list = []
                for row in dict_reader:
                    new_dict = {}
                    for key, value in row.items():
                        new_dict[key] = int(value)
                    new_list.append(new_dict)

                #create the object
                for row in new_list:
                    created_list.append(cls.create(**row))
                return created_list
        except IOError:
            return ([])
