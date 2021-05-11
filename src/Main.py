import sys

import numpy as np
from PIL import Image
from RayCasting import RayCasting
from Color import Color
from Camera import Camera
from Sphere import Sphere
from Triangle import Triangle

#Anwendung/Bild
_HEIGHT = 400
_WIDTH = 400
_BACKGROUND_COLOR = Color(0, 0, 0) #schwarz

#Kamera
#def __init__(self, eye, up, center, fov):
_EYE = np.array([0, 1.8, 10])
_UP = np.array([0, 1, 0])
_CENTRE = np.array([0, 3, 0])
_FOV = 45
_ASPECT_RATIO = _HEIGHT / _WIDTH

#Bild erzeugen
image = Image.new('RGB', (_WIDTH, _HEIGHT))

#Kugel erzeugen
kugel1 = Sphere(np.array([1.5, 4.1, 1]), 1.2, Color(255, 0, 0))
kugel2 = Sphere(np.array([0, 2, 0.5]), 1.2, Color(0, 0, 255))
kugel3 = Sphere(np.array([-1.5, 4.1, 1]), 1.2, Color(0, 255, 0))

#Dreieck erzeugen               #a                         #b                      #c
dreieck = Triangle(np.array([1.5, 4.1, 1]), np.array([0, 2, 0.5]), np.array([-1.5, 4.1, 1]), Color(255, 255, 0))

#objectlist
objectlist= []

objectlist.append(kugel1)
objectlist.append(kugel2)
objectlist.append(kugel3)
objectlist.append(dreieck)

#RayCasting
#def __init__(self, imageWidth, imageHeight, objectlist, background_color, image, camera):
rc = RayCasting(_WIDTH, _HEIGHT, objectlist, _BACKGROUND_COLOR, image, Camera(_EYE, _UP, _CENTRE, _FOV))
rc.start()

image.show()
image.save("image.jpg")

sys.exit()