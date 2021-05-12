import sys

import numpy as np
from PIL import Image
from RayCasting import RayCasting
from Color import Color
from Camera import Camera
from Sphere import Sphere
from Triangle import Triangle
from Lightsource import Lightsource
from Surface import Surface
from Plane import Plane
from CheckerBoardMaterial import CheckerBoardMaterial

#Anwendung/Bild
_HEIGHT = 400
_WIDTH = 400
_BACKGROUND_COLOR = Color(0,0,0)

#Kamera
#def __init__(self, eye, up, center, fov):
_EYE = np.array([0, 2, 5])
_UP = np.array([0, 1, 0])
_CENTRE = np.array([0, 1, 8])
_FOV = 45
_ASPECT_RATIO = _HEIGHT / _WIDTH

#Lichtquelle
lightsource = Lightsource(np.array([-20, -20, 3]))

#Bild erzeugen
image = Image.new('RGB', (_WIDTH, _HEIGHT))

#Kugel erzeugen
kugel1 = Sphere(np.array([2.5, 1, 17]), 1.9, Surface(lightsource, Color(0, 255, 0)))
kugel2 = Sphere(np.array([-2.5, 1, 17]), 1.9, Surface(lightsource, Color(255, 0, 0)))
kugel3 = Sphere(np.array([0, -3, 17]), 1.9, Surface(lightsource, Color(0, 0, 255)))

#Dreieck erzeugen               #a                         #b                      #c
dreieck = Triangle(np.array([2.5, 1, 7]),
                   np.array([0, -3, 17]),
                   np.array([-2.5, 1, 17]),
                   Surface(lightsource, Color(255, 255, 0)))

#plane = Plane(np.array([0, 3.5, 0]), np.array([0, -1, 0]))

#objectlist
objectlist= []

objectlist.append(kugel1)
objectlist.append(kugel2)
objectlist.append(kugel3)
objectlist.append(dreieck)
#objectlist.append(plane)

#RayCasting
checker = CheckerBoardMaterial()
rc = RayCasting(_WIDTH, _HEIGHT, objectlist, _BACKGROUND_COLOR, image, Camera(_EYE, _UP, _CENTRE, _FOV), lightsource, checker)
rc.start()

image.show()
image.save("image.jpg")

sys.exit()