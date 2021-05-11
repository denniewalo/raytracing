import numpy as np
import math as math
class Sphere(object):
    def __init__(self, center, radius):
        self.center = center #punkt
        self.radius = radius #skalar

    def __repr__(self):
        return "Sphere(%s,%s" %(repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v*v - co.dot(co) + self.radius*self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        return self.normalized(p - self.center)

    def normalized(self, vecPC):
        vecLength = np.sqrt(vecPC.dot(vecPC))
        return np.array(vecPC/vecLength)
