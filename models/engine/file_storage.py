#!/usr/bin/env python3
# This class serializes instance to a JSON file and deserializes JSON file
# to a instance
"""Represent class FileStorage."""
from models.base_model import BaseModel
from os import path
import json


class FileStorage:
    """Define class FileStorage

    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): stores all objects

    Methods:
        all(): returns the dictionary objects
        new(): sets ib __objects the obj with key
        save(): serializes __objects to the JSON file (path: __file_path)
        reload(): deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists; otherwise, do nothing. if the file
        doesn't exist no exception should be raised
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """set in objects the obj with key <obj class name>.id

        Attributes:
        obj (obj): object to set in objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as fd:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.
                       items()}, fd)

    def reload(self):
        """deserializes the JSON file to objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. if the file doesnt exist,
        no exception is raised)
        """
        if path.exists(self.__file_path) is False:
            return
        with open(self.__file_path, mode='r') as fd:
            deserialized = None
            try:
                deserialized = json.load(fd)
            except Exception as e:
                return
