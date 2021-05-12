from Color import Color
class Lightsource(object):
    def __init__(self, source):
        self.source = source
        self.color = Color(200, 200, 200)

    def getColor(self):
        return self.color