from typing import TypeVar, Generic
from abc import *

T = TypeVar('T')


def white():
    return "ffffff"


class Type(Generic[T]):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_r(self):
        return self.r

    def get_g(self):

        return self.g

    def get_b(self):
        return self.b