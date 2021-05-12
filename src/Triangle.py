import numpy as np
from Surface import Surface
from Color import Color

class Triangle(object):
    def __init__(self, a, b, c, surface):
        self.a = a # a point
        self.b = b # b point
        self.c = c # c point
        self.surface = surface #color
        self.u = self.b - self.a #direction vector
        self.v = self.c - self.a #direction vector

    def __repr__(self):
        return "Triangle(%s,%s,%s)" %(repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = np.cross(ray.direction, self.v)
        #dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = np.cross(w, self.u)
        #wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0<=r and r<=1 and 0<=s and s<=1 and r+s<=1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        return self.normalized(np.cross(self.u, self.v))

    def normalized(self, p):
        vecLength = np.sqrt(p.dot(p))
        return np.array(p/vecLength)

    def colorAt(self, ray, light_dir, intersectionPoint_normal, ls, collide):
        if collide:
            return self.colorAmb(self.surface.getColor()).getColor()
        color = self.surface.getColor()
        #Ambient
        colorAmb = self.colorAmb(color)
        #Diff
        colorDif = self.colorDif(intersectionPoint_normal, light_dir)
        #Spec
        colorSpe = self.colorSpe(intersectionPoint_normal, light_dir, ray)
        color = color * (colorAmb + colorDif + colorSpe)
        color = Color.divColor(color, 255)
        return color.getColor()

    def colorAmb(self, color):
        color = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getAmbient())
        return color

    def colorDif(self, normal, light_dir):
        skalar = np.dot(normal, light_dir.direction)
        dif = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getDiffuse())
        return Color.multiplayColor(dif, skalar)

    def colorSpe(self, normal, light_dir, ray):
        skalar = np.dot(normal, light_dir.direction)
        normal = normal * (2*skalar)
        lr = light_dir.direction - normal
        skalarLr = np.dot(lr, (ray.direction*-1))
        colorSpe = Color.multiplayColor(self.surface.ls.getColor(), self.surface.getSpecular())
        return Color.multiplayColor(colorSpe, (skalarLr**20.0))