import math
import numpy as np

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalized(self):
        return self.x, self.y, self.z

    def getLength(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def lengthDivision(self, divLen):
        return Vector(self.x/divLen, self.y/divLen, self.z/divLen)

    def crossproduct(self, other):
        return Vector(((self.y * other.z) - (self.z * other.y)),
                      ((self.z * other.x) - (self.x * other.z)),
                      ((self.x * other.y) - (self.y * other.x)))

