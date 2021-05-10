class RayCasting(object):
    def __init__(self, imageWidth, imageHeight, objectlist):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.objectlist = objectlist

    def start(self):
        for x in range(self.imageWidth):
            for y in range(self.imageHeight):
                ray = calcRay(x, y)
                maxdist = float("inf")
                color = BACKGROUND_COLOR
                for object in self.objectlist:
                    hitdist = object.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            color = object.colorAt(ray)
                image.pupixel((x,y), color)