from Color import Color

class Surface(object):
    def __init__(self, ls, color=Color(255, 255, 255), ambient=0.7, diffuse=0.5, specular=0.3):
        self.color = color
        self.ls = ls
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def getColor(self):
        return self.color

    def getAmbient(self):
        return self.ambient

    def getDiffuse(self):
        return self.diffuse

    def getSpecular(self):
        return self.specular