from Vector import Vector

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
        vectorF = Vector.lengthDivision(self.center - self.eye, Vector.getLength(self.center - self.eye))
        return vectorF

    def calcS(self):
        vectorS = Vector.lengthDivision(Vector.crossproduct(self.f, self.up),
                                        Vector.getLength(Vector.crossproduct(self.f, self.up)))
        return vectorS

    def calcU(self):
        vectorU = Vector.crossproduct(self.s, self.f)
        return vectorU


