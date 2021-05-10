import numpy as np

class Camera(object):
    def __init__(self, eye, directionOfView, up, center):
        self.eye = eye
        self.directionOfView = directionOfView
        self.up = up
        self.center = center
        self.f = self.calcF()
        self.s = self.calcS()
        self.u = self.calcU()

    def calcF(self):
        #numpy f = (c-e) / ||c-e||
        return np.array(self.subDivisionLength(self.center, self.eye))

    def calcS(self):
        #numpy s = f x up / || f x up ||
        return np.array(self.crossDivisionLength(self.f, self.up))

    def calcU(self):
        #numpy
        return np.cross(self.s, self.f)


    def subDivisionLength(self, vectorA, vectorB):
        #return res = (a-b) / ||a-b||
        return (vectorA - vectorB) / np.sqrt((vectorA-vectorB).dot(vectorA-vectorB))

    def crossDivisionLength(self, vectorA, vectorB):
        #return res = a x b / || a x b ||
        return np.cross(vectorA, vectorB) / np.sqrt((np.cross(vectorA, vectorB).dot(np.cross(vectorA, vectorB))))

