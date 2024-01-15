#!/usr/bin/python3
"""base.py"""
import json
import os
import csv
import turtle


class Base:
    """Defines a base model class."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file:"""
        if list_objs:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        else:
            jsons = '[]'
        with open(cls.__name__+'.json', 'w') as file_object:
            file_object.write(jsons)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            redefine = cls(1)
        if cls.__name__ == 'Rectangle':
            redefine = cls(1, 1)
        if redefine:
            redefine.update(**dictionary)
            return redefine

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if os.path.exists(cls.__name__ + '.json'):
            with open(cls.__name__ + '.json', 'r') as file_object:
                list_dicts = cls.from_json_string(file_object.read())
            return [cls.create(**dic) for dic in list_dicts]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        if list_objs:
            csvs = [x.to_dictionary() for x in list_objs]
        else:
            csvs = '[]'
        # field_names = []
        keys = csvs[0].keys()
        with open(cls.__name__ + '.csv', 'w') as file_object:
            write = csv.DictWriter(file_object, keys)
            write.writeheader()
            write.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        if os.path.exists(cls.__name__ + '.csv'):
            with open(cls.__name__ + '.csv', 'r') as file_object:
                reader = csv.DictReader(file_object)
                fieldNames = [row for row in reader]
                for row in fieldNames:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except:
                            pass
            return [cls.create(**dic) for dic in fieldNames]
        else:
            return []

    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.bgcolor('#EBECED')
        brad = turtle.Turtle()
        brad.pensize(3)
        turtle.register_shape("resized_circle",
                              ((0, 1), (1, 0), (1, 1), (1, 1)))
        brad.shape("resized_circle")
        brad.pencolor("#194a7a")
        for rect in list_rectangles:
            brad.penup()
            brad.goto(rect.x, rect.y)
            brad.pendown()

            brad.forward(rect.width)
            brad.left(90)
            brad.forward(rect.height)
            brad.left(90)
            brad.forward(rect.width)
            brad.left(90)
            brad.forward(rect.height)
            brad.left(90)
        brad.pencolor("#008585")
        for squ in list_squares:
            brad.penup()
            brad.goto(squ.x, squ.y)
            brad.pendown()

            brad.forward(squ.width)
            brad.left(90)
            brad.forward(rect.height)
            brad.left(90)
            brad.forward(squ.width)
            brad.left(90)
            brad.forward(rect.height)
            brad.left(90)
