import inspect
import sys
from pprint import pprint


class Cars:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age


obj_1 = Cars('Audi', 10)


def introspection_info(obj):
    res_dict = {'type': type(obj), 'attributes': obj.__dict__, 'methods': dir(obj), 'module': inspect.getmodule(obj),
                'memory': sys.getsizeof(obj), 'id': id(obj)}
    return res_dict,


pprint(introspection_info(obj_1))
