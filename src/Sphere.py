import numpy as np
import math as math
from Surface import Surface
from Color import Color
from Ray import Ray
from Lightsource import Lightsource

class Sphere(object):
    def __init__(self, center, radius, surface):
        self.center = center #punkt
        self.radius = radius #skalar
        self.surface = surface

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

    def colorAt(self, ray, light_dir, intersectionPoint_normal, ls, collide):
        if collide:
            color = Color.multiplayColor(self.surface.getColor(), self.surface.getAmbient())
            return color.getColor()

        color = self.surface.getColor()
        #Ambient
        colorAmb = self.colorAmb(color)
        #Diff
        colorDif = self.colorDif(intersectionPoint_normal, light_dir)
        #Spec
        colorSpe = self.colorSpe(intersectionPoint_normal, light_dir, ray)

        black = colorAmb + colorDif + colorSpe
        return black.getColor()

    def colorAmb(self, color):
        color = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getAmbient())
        return color

    def colorDif(self, normal, light_dir):
        skalar = np.dot(normal, light_dir.direction)
        dif = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getDiffuse())
        return Color.multiplayColor(dif, skalar)


    def colorSpe(self, normal, light_dir, ray):
        lr = self.calcLr(normal, light_dir)
        skalar = np.dot(lr, (self.normalized(ray.direction) * -1))
        colorSpe = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getSpecular())
        return Color.multiplayColor(colorSpe, (skalar**10.))


    def calcLr(self, normal, light_dir):
        skalar = np.dot(normal, light_dir.direction)
        normal = normal * (2*skalar)
        return light_dir.direction - normal

