import numpy as np
from Lightsource import Lightsource
from Color import Color
from Ray import Ray
from Plane import Plane
from CheckerBoardMaterial import CheckerBoardMaterial
class RayCasting(object):
    def __init__(self, imageWidth, imageHeight, objectlist, background_color, image, camera, lightsource, checkerBoard):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.objectlist = objectlist
        self.background_color = background_color
        self.image = image
        self.camera = camera
        self.aspectratio = self.imageHeight / self.imageWidth
        self.height = self.calcHeight(self.alpha())
        self.width = self.calcWidth(self.aspectratio)
        self.pixelWidth = self.calcPixelWidth()
        self.pixelHeight = self.calcPixelHeight()
        self.lightsource = lightsource
        self.checkerBoard = checkerBoard

    def start(self):
        for x in range(self.imageWidth):
            for y in range(self.imageHeight):
                ray = self.camera.calcRay(x, y, self.pixelHeight, self.pixelWidth, self.width, self.height) #Berechnet den Strahl, der durch den Pixel geht
                maxdist = float('inf') #Max Reichweite angeben -> bei uns "inf" für infinity (größtmöglicher float-wert)
                color = self.background_color.getColor()  #Wenn der Strahl kein Objekt schneided, so ist die Farbe an dieser Stelle, die Hintergrundfarbe (weil kein Objekt)
                for ob in self.objectlist:
                    hitdist = ob.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            intersectionPoint = ray.pointAtParameter(maxdist)
                            #Schnittpunkt normale
                            intersectionPoint_normal = ob.normalAt(intersectionPoint)
                            #Lichtstrahl vom Schnittpunkt zur Lichtquelle
                            light_dir = Ray(intersectionPoint, self.lightsource.source - intersectionPoint)
                            collide = False
                            if(self.collideObject(light_dir)):
                                collide = True
                                if(isinstance(ob, Plane)):
                                    color = CheckerBoardMaterial.ColorAt(self.checkerBoard, intersectionPoint, collide)
                                else:
                                    color = ob.colorAt(ray, light_dir, intersectionPoint_normal,self.lightsource, collide)
                            else:
                                if(isinstance(ob, Plane)):
                                    color = CheckerBoardMaterial.ColorAt(self.checkerBoard, intersectionPoint, collide)
                                else:
                                    color = ob.colorAt(ray, light_dir, intersectionPoint_normal, self.lightsource, collide)
                self.image.putpixel((x, y), color)

    def collideObject(self, light_dir):
        for ob in self.objectlist:
            hitdist = ob.intersectionParameter(light_dir)
            if hitdist and hitdist > 0:
                return True
        return False

    def alpha(self):
        return self.camera.fov/2

    def calcHeight(self, angle):
        return 2*np.tan(angle)

    def calcWidth(self, aspectratio):
        return aspectratio*self.calcHeight(self.alpha())

    def calcPixelWidth(self):
        return self.width / (self.imageWidth - 1)

    def calcPixelHeight(self):
        return self.height / (self.imageHeight -1)