class RayCasting(object):
    def __init__(self, imageWidth, imageHeight, objectlist):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.objectlist = objectlist

    def start(self):
        for x in range(self.imageWidth):
            for y in range(self.imageHeight):
                ray = calcRay(x, y) #Berechnet den Strahl, der durch den Pixel geht
                maxdist = float('inf') #Max Reichweite angeben -> bei uns "inf" für infinity (größtmögliche float-wert)
                color = BACKGROUND_COLOR #Wenn der Strahl kein Objekt schneided, so ist die Farbe an dieser Stelle, die Hintergrundfarbe (weil kein Objekt)
                for object in self.objectlist:
                    hitdist = object.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            color = object.colorAt(ray)
                image.putpixel((x,y), color)