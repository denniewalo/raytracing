import numpy as np
from Ray import Ray

class Camera(object):
    def __init__(self, eye, up, center, fov):
        self.eye = eye
        self.up = up
        self.center = center
        self.fov = fov
        self.f = self.calculateF()
        print(self.f)
        self.s = self.calculateS()
        print(self.s)
        self.u = self.calculateU()
        print(self.u)

    def calculateF(self):
        #numpy f = (c-e) / ||c-e||
        return np.array(self.subDivisionLength(self.center, self.eye))

    def calculateS(self):
        #numpy s = f x up / || f x up ||
        return np.array(self.crossDivisionLength(self.f, self.up))

    def calculateU(self):
        #numpy
        return np.cross(self.s, self.f)

    def calcRay(self, x, y, pixelWidth, pixelHeight, width, height):
        xcomp = self.s * (x * pixelWidth - width/2)
        ycomp = self.u * (y * pixelHeight - height/2)
        return Ray(self.eye, self.f + xcomp + ycomp)

    def subDivisionLength(self, vectorA, vectorB):
        #return res = (a-b) / ||a-b||
        return (vectorA - vectorB) / np.sqrt((vectorA-vectorB).dot(vectorA-vectorB))

    def crossDivisionLength(self, vectorA, vectorB):
        #return res = a x b / || a x b ||
        return np.cross(vectorA, vectorB) / np.sqrt((np.cross(vectorA, vectorB).dot(np.cross(vectorA, vectorB))))

