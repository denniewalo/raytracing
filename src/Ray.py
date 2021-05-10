import numpy as np


class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin #Ausgangspunkt, in der Regel Kamerazentrum
        self.direction = self.normalized(direction)

    def __repr__(self):
        return "Ray(%s,%s)" %(repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        return self.origin + (self.direction * t) #Vektorskalierung

    def normalized(self, direction):
        vecLength = np.sqrt(direction.dot(direction))
        return np.array(direction/vecLength)

