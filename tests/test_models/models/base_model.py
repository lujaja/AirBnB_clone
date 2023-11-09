#!/usr/bin/env python3
# This class define all common attributes for othe classes
"""Define BaseModel"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseMode representation.

    Attributes:
        id (str): unique user identifier for each instantiated instance
        created_at (str): instatiation time for instance
        updated_at (str): time an instance is changed

    Methods:
        __str__ (magic method): should print
        sale(): updates updated at with the curent date and time
        to_dict(): return dictionary containing all keys/values of
        __dict__ of instance
    """
    def __init__(self, *args, **kwargs):
        """instatiate an object with its attributes
        Attributes:
            args: will not be used
            kwargs: will be used if vailbale
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>
        """
        fmt = "[{}] ({}) {}"
        return fmt.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute (updated_at)
        with current time
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance
        """
        dik = {**self.__dict__}
        dik['__class__'] = type(self).__name__
        dik["created_at"] = dik["created_at"].isoformat()
        dik["updated_at"] = dik["updated_at"].isoformat()
        return dik
