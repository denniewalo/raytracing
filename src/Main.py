import numpy as np

#Anwendung
_HEIGHT = 600
_WIDTH = 600
_BACKGROUND_COLOR = None

#Kamera
_EYE = np.array([])
_UP = np.array([])
_CENTRE = np.array([])
_FOV = 45
_ASPECT_RATIO = _HEIGHT / _WIDTH

print(np.tan(_FOV/2))